Summary:	Wine-Doors - Windows application management for the GNOME desktop
Summary(pl.UTF-8):	Wine-Doors - zarządzanie aplikacjami Windows dla środowiska GNOME
Name:		wine-doors
Version:	0.1.4
%define	_rc	a2
Release:	0.%{_rc}.0.9
License:	GPL (application), Creative Commons (artwork)
Group:		Applications/Emulators
Source0:	http://sourceforge.net/projects/winedoors/files/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	78d5acd1b65bee9cd08b0a2b31ad8d45
Patch0:		%{name}-runtime-deps.patch
#URL:		http://www.wine-doors.org/	Dead URL
URL:		http://sourceforge.net/projects/winedoors/
BuildRequires:	synce-orange
Requires:	cabextract
Requires:	cairo >= 1.2.4
Requires:	python
Requires:	python-gnome-desktop-librsvg >= 2.16
Requires:	python-libxml2
Requires:	python-pycairo >= 1.2.0
Requires:	python-pygtk-glade
Requires:	synce-orange
Requires:	which
Requires:	wine
Requires:	wine-programs
Requires:	xorg-app-setxkbmap
#BuildArch:	noarch
ExclusiveArch:	%{ix86}
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no binary contents
%define		_enable_debug_packages	0

%description
Wine-doors provides a replacement for winetools which adds apt/yum
functionality to wine, doing away with the bad aspects of winetools
whilst keeping the good ones and extending on the origninal idea with
a more modern design approach.

Wine-Doors is licensed under the GNU General Public License and
utilises resources from the Tango Project.

%description -l pl.UTF-8
Wine-doors dostarcza zamiennik winetools dodający funkcjonalność
apt/yum do wine, unikając złych aspektów winetools, a zachowując dobre
i rozszerzając oryginalny pomysł o bardziej współczesne podejście.

Wine-Doors jest udostępniany na Powszechnej Licencji Publicznej GNU
(General Public License) i wykorzystuje zasoby z projektu Tango.

%prep
%setup -q -c -n %{name}-%{version}%{_rc}
#patch0 -p1

cat <<'EOF' > %{name}.sh
#!/bin/sh
exec %{__python} %{_datadir}/%{name}/src/winedoors.pyo
EOF

%{__sed} -i -e '1s,#.*python,#!%{__python},' src/winedoors.py

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
export USER=root
%{__python} setup.py install \
	--temp=$RPM_BUILD_ROOT \
	--config=%{_sysconfdir}/%{name} \
	-S

rm -f $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}/src
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}/src
%py_postclean %{_datadir}/%{name}/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENSE README
%dir %{_sysconfdir}/wine-doors
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/preferences.xml
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/wine-doors.desktop
%{_pixmapsdir}/wine-doors.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dtd
%{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/registry
%dir %{_datadir}/%{name}/src
%{_datadir}/%{name}/src/*.png
%{_datadir}/%{name}/src/*.sh
%{_datadir}/%{name}/src/*.svg
%{_datadir}/%{name}/src/winedoors.glade
%{_datadir}/%{name}/src/winedoors.gladep
%{_datadir}/%{name}/src/*.py[co]
## Repositories should be as separate package?
%dir %{_datadir}/%{name}/applications.repo
%dir %{_datadir}/%{name}/base.repo
%dir %{_datadir}/%{name}/games.repo
%dir %{_datadir}/%{name}/libraries.repo
%{_datadir}/%{name}/applications.repo/*.wdi
%{_datadir}/%{name}/base.repo/*.wdi
%{_datadir}/%{name}/games.repo/*.wdi
%{_datadir}/%{name}/libraries.repo/*.wdi
%{_datadir}/%{name}/applications.repo/*.xml.gz
%{_datadir}/%{name}/base.repo/*.xml.gz
%{_datadir}/%{name}/games.repo/*.xml.gz
%{_datadir}/%{name}/libraries.repo/*.xml.gz

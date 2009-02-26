Summary:	Wine-Doors - Windows application management for the GNOME desktop
Summary(pl.UTF-8):	Wine-Doors - zarządzanie aplikacjami Windows dla środowiska GNOME
Name:		wine-doors
Version:	0.1.3
Release:	2
License:	GPL (application), Creative Commons (artwork)
Group:		Applications/Emulators
Source0:	http://wddb.wine-doors.org/system/files/%{name}-%{version}rc1.tar_.gz
# Source0-md5:	09b243103f7f733f3cd4ce694d5af3b6
Patch0:		%{name}-runtime-deps.patch
URL:		http://www.wine-doors.org/
Requires:	cabextract
Requires:	cairo >= 1.2.4
Requires:	python
Requires:	python-gnome-desktop-librsvg >= 2.16
Requires:	python-libxml2
Requires:	python-pycairo >= 1.2.0
Requires:	python-pygtk-glade
Requires:	which
Requires:	wine
Requires:	wine-programs
Requires:	xorg-app-setxkbmap
#BuildArch:	noarch
ExclusiveArch:	%{ix86}
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n %{name}-%{version}rc1
%patch0 -p1

cat <<'EOF' > %{name}.sh
#!/bin/sh
exec %{__python} %{_datadir}/%{name}/src/winedoors.pyo
EOF

%{__sed} -i -e '1s,#.*python,#!%{__python},' src/winedoors.py

%install
rm -rf $RPM_BUILD_ROOT

export USER=root
python setup.py install \
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

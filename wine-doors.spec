%define		_pre	pre1
%define		_rel	0.3
Summary:	Wine-Doors - Windows application management for the GNOME desktop
Summary(pl.UTF-8):	Wine-Doors - zarządzanie aplikacjami Windows dla środowiska GNOME
Name:		wine-doors
Version:	0.1
Release:	1.%{_pre}.%{_rel}
License:	GPL (application), Creative Commons (artwork)
Group:		Applications/Emulators
Source0:	http://www.wine-doors.org/releases/%{name}-%{version}%{_pre}.tar.gz
# Source0-md5:	03db43c3af6dd6e21a49da428d80fa21
URL:		http://www.wine-doors.org/
BuildRequires:	rpm-pythonprov
Requires:	cairo >= 1.2.4
Requires:	python
Requires:	python-gnome-desktop-librsvg >= 2.16
Requires:	python-libxml2
Requires:	python-pycairo >= 1.2.0
Requires:	python-pygtk-glade
Requires:	which
Requires:	wine
#Requires:	wine-programs
BuildArch:	noarch
ExclusiveArch:	%{ix86} noarch
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
%setup -q -n %{name}-%{version}%{_pre}

cat <<'EOF' > %{name}.sh
#!/bin/sh
exec %{__python} %{_datadir}/%{name}/src/winedoors.pyo
EOF

%{__sed} -i -e '1s,#.*python,#!%{__python},' src/winedoors.py

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install -S \
	--temp=$RPM_BUILD_ROOT \
	--prefix=/ \
	--config=%{_sysconfdir}/%{name}

rm -f $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}/src
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}/src
%py_postclean %{_datadir}/%{name}/src
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/src/*.bak

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENSE README
%dir %{_sysconfdir}/wine-doors
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/preferences.xml
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/wine-doors.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/base.repo
%{_datadir}/%{name}/global.repo
%{_datadir}/%{name}/games.repo
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

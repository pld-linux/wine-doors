%define		_snap	20061221.386
%define		_rel	0.2
Summary:	Wine-Doors - Windows application management for the GNOME desktop
Name:		wine-doors
Version:	0.1
Release:	0.%{_snap}.%{_rel}
License:	GPL (application), Creative Commons (artwork)
Group:		Applications/Emulators
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	d39448dc6cca0ba00d5a8c5735da92ef
Patch0:		%{name}-rootdir.patch
URL:		http://www.wine-doors.org/
Requires:	python
#Requires:	wine
#Requires:	wine-programs
BuildArch:	noarch
ExclusiveArch:	%{ix86} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wine-doors provides a replacement for winetools which adds apt/yum
functionality to wine, doing away with the bad aspects of winetools
whilst keeping the good ones and extending on the origninal idea with
a more modern design approach.

Wine-Doors is licensed under the GNU general public license and
utilises resources from the Tango Project.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--prefix=%{_prefix}

ln -sf %{_datadir}/%{name}/src/winedoors.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}/src
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}/src
#py_postclean %{_datadir}/%{name}/src

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
%{_datadir}/%{name}/dtd
%{_datadir}/%{name}/pixmaps
%dir %{_datadir}/%{name}/src
%{_datadir}/%{name}/src/*.svg
%{_datadir}/%{name}/src/*.xml
%{_datadir}/%{name}/src/*.png
%{_datadir}/%{name}/src/winedoors.glade
%{_datadir}/%{name}/src/winedoors.gladep
%{_datadir}/%{name}/src/*.py[co]
%attr(755,root,root) %{_datadir}/%{name}/src/*.py

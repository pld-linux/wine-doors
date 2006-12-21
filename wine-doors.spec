%define		_snap	20061221.386
%define		_rel	0.1
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
#Requires:	wine
#Requires:	wine-programs
BuildArch:	noarch
ExclusiveArch:	%{ix86} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_winetoolsdir	%{_datadir}/%{name}

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

%py_comp $RPM_BUILD_ROOT%{_datadir}/wine-doors/src
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/wine-doors/src
%py_postclean %{_datadir}/wine-doors/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENSE README
%dir %{_sysconfdir}/wine-doors
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wine-doors/preferences.xml

%{_desktopdir}/wine-doors.desktop

%dir %{_datadir}/wine-doors
%{_datadir}/wine-doors/base.repo
%{_datadir}/wine-doors/global.repo
%{_datadir}/wine-doors/dtd
%{_datadir}/wine-doors/pixmaps

%dir %{_datadir}/wine-doors/src
%{_datadir}/wine-doors/src/*.svg
%{_datadir}/wine-doors/src/*.xml
%{_datadir}/wine-doors/src/*.png
%{_datadir}/wine-doors/src/winedoors.glade
%{_datadir}/wine-doors/src/winedoors.gladep
%{_datadir}/wine-doors/src/*.py[co]

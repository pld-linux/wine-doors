# TODO
# - build: which: no wine in (/bin:/usr/bin:/usr/sbin:/sbin:/usr/X11R6/bin)
%define		_snap	20070203.420
%define		_rel	0.1
Summary:	Wine-Doors - Windows application management for the GNOME desktop
Summary(pl):	Wine-Doors - zarz±dzanie aplikacjami Windows dla ¶rodowiska GNOME
Name:		wine-doors
Version:	0.1
Release:	0.%{_snap}.%{_rel}
License:	GPL (application), Creative Commons (artwork)
Group:		Applications/Emulators
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	fbb9f9f5fe587004a0a8e049fb4672cf
Patch0:		%{name}-rootdir.patch
Patch1:		%{name}-wineroot.patch
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

Wine-Doors is licensed under the GNU General Public License and
utilises resources from the Tango Project.

%description -l pl
Wine-doors dostarcza zamiennik winetools dodaj±cy funkcjonalno¶æ
apt/yum do wine, unikaj±c z³ych aspektów winetools, a zachowuj±c dobre
i rozszerzaj±c oryginalny pomys³ o bardziej wspó³czesne podej¶cie.

Wine-Doors jest udostêpniany na Powszechnej Licencji Publicznej GNU
(General Public License) i wykorzystuje zasoby z projektu Tango.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

cat <<'EOF' > %{name}.sh
#!/bin/sh
exec %{__python} %{_datadir}/%{name}/src/winedoors.pyo
EOF

%{__sed} -i -e '1s,#.*python,#!%{__python},' src/winedoors.py

%install
rm -rf $RPM_BUILD_ROOT

export USER=root # to fool setup.py with wineroot detection

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--prefix=%{_prefix}

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

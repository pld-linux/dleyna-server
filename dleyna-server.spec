Summary:	Service for interacting with Digital Media Servers
Name:		dleyna-server
Version:	0.5.0
Release:	1
License:	LGPL v2
Group:		Applications
Source0:	https://01.org/sites/default/files/downloads/dleyna/%{name}-%{version}.tar.gz
# Source0-md5:	38c58ea3eb3a181f2cd9ff75f9a5fa6d
# https://github.com/01org/dleyna-server/issues/145
Patch0:		0001-Device-Fix-ChildCount-property-type.patch
URL:		https://01.org/dleyna/
BuildRequires:	autoconf >= 2.66
BuildRequires:	automake
BuildRequires:	dleyna-core-devel >= 0.5.0
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gssdp-devel >= 0.13.2
BuildRequires:	gupnp-av-devel >= 0.11.5
BuildRequires:	gupnp-devel >= 0.20.3
BuildRequires:	gupnp-dlna-devel >= 0.9.4
BuildRequires:	libsoup-devel >= 2.28.2
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig >= 1:0.16
Requires:	dleyna-connector-dbus
Requires:	dleyna-core >= 0.5.0
Requires:	glib2 >= 1:2.28.0
Requires:	gssdp >= 0.13.2
Requires:	gupnp >= 0.20.3
Requires:	gupnp-av >= 0.11.5
Requires:	gupnp-dlna >= 0.9.4
Requires:	libsoup >= 2.28.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-Bus service for clients to discover and manipulate DLNA Digital
Media Servers (DMSes).

%package devel
Summary:	Development files for dLeyna server
Group:		Development/Libraries
# does not require base package
Requires:	dleyna-core-devel >= 0.5.0
Requires:	glib2-devel >= 1:2.28.0

%description devel
This package provides development files for dLeyna server.

%prep
%setup -q
%patch0 -p1


%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/dleyna-server/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libexecdir}/dleyna-server-service
%dir %{_libdir}/dleyna-server
%attr(755,root,root) %{_libdir}/dleyna-server/libdleyna-server-1.0.so*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dleyna-server-service.conf
%{_datadir}/dbus-1/services/com.intel.dleyna-server.service

%files devel
%defattr(644,root,root,755)
%{_includedir}/dleyna-1.0/libdleyna/server
%{_pkgconfigdir}/dleyna-server-service-1.0.pc

# see m4/${libname}.m4 />= for required version of particular library
%define		libcdata_ver	20160108
%define		libcerror_ver	20120425
%define		libcthreads_ver	20160404
Summary:	Library to provide generic file data cache functions
Summary(pl.UTF-8):	Biblioteka udostępniająca funkcje do ogólnego buforowania danych z plików
Name:		libfcache
Version:	20181011
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libfcache/releases
Source0:	https://github.com/libyal/libfcache/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	23647e6947fae9075d457551de3580d7
URL:		https://github.com/libyal/libfcache/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcthreads >= %{libcthreads_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfcache is a library to provide generic file data cache functions.

%description -l pl.UTF-8
libfcache to biblioteka udostępniająca funkcje do ogólnego buforowania
danych z plików błędów w C.

%package devel
Summary:	Header files for libfcache library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfcache
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}

%description devel
Header files for libfcache library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfcache.

%package static
Summary:	Static libfcache library
Summary(pl.UTF-8):	Statyczna biblioteka libfcache
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfcache library.

%description static -l pl.UTF-8
Statyczna biblioteka libfcache.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfcache.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libfcache.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfcache.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfcache.so
%{_includedir}/libfcache
%{_includedir}/libfcache.h
%{_pkgconfigdir}/libfcache.pc
%{_mandir}/man3/libfcache.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfcache.a

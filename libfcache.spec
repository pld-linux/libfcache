Summary:	Library to provide generic file data cache functions
Summary(pl.UTF-8):	Biblioteka udostępniająca funkcje do ogólnego buforowania danych z plików
Name:		libfcache
Version:	20150104
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libfcache/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bad6ee41c037038a6ea4561a7b4825b4
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libfcache/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcdata-devel >= 20130407
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcdata >= 20130407
Requires:	libcerror >= 20120425
Requires:	libcstring >= 20120425
Requires:	libcthreads >= 20130509
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
Requires:	libcdata-devel >= 20130407
Requires:	libcerror-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509

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
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
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

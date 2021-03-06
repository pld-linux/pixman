#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Pixel manipulation library
Summary(pl.UTF-8):	Biblioteka operacji na pikselach
Name:		pixman
# 0.38.x is stable, 0.39.x unstable
Version:	0.40.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://www.cairographics.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	73858c0862dd9896fb5f62ae267084a4
URL:		http://pixman.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
%{?with_tests:BuildRequires:	libpng-devel}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.453
BuildRequires:	sed >= 4.0
Obsoletes:	libic
Obsoletes:	libpixman
Obsoletes:	libpixregion
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pixman is a pixel manipulation library.

%description -l pl.UTF-8
pixman to biblioteka do operacji na pikselach.

%package devel
Summary:	Development files for pixman
Summary(pl.UTF-8):	Pliki dla programistów do biblioteki pixman
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libic-devel
Obsoletes:	libpixman-devel
Obsoletes:	libpixregion-devel

%description devel
This package contains development files for pixman library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki dla programistów korzystających z biblioteki
pixman.

%package static
Summary:	Static pixman library
Summary(pl.UTF-8):	Statyczna biblioteka pixman
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libic-static
Obsoletes:	libpixman-static
Obsoletes:	libpixregion-static

%description static
This package contains static pixman library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki pixman.

%prep
%setup -q

%{__sed} -i -e 's#<pixman-version.h>#"pixman-version.h"#' pixman/pixman.h

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk \
	--disable-openmp \
	--disable-silent-rules \
%ifarch %{x8664}
%if "%{cc_version}" < "4.2"
	--disable-sse2
%endif
%endif

%{__make}

%{?with_tests:%{__make} -j1 check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libpixman-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpixman-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpixman-1.so
%{_libdir}/libpixman-1.la
%{_includedir}/pixman-1
%{_pkgconfigdir}/pixman-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpixman-1.a

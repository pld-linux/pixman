Summary:	Pixel manipulation library
Summary(pl.UTF-8):	Biblioteka operacji na pikselach
Name:		pixman
Version:	0.11.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
# Source0-md5:	7ba370232a93cddfdaac1a0b180b6a92
Patch0:		%{name}-gcc3.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.453
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
%if "%{cc_version}" < "3.4"
%patch0 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -i -e 's#<pixman-version.h>#<pixman-1/pixman-version.h>#g' $RPM_BUILD_ROOT%{_includedir}/pixman-1/pixman.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
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

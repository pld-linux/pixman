Summary:	Biblioteka operacji na pikselach
Summary:	Pixel manipulation library
Name:		pixman
Version:	0.9.4
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.gz
# Source0-md5:	44851d2c6015c5c5794c2f2041cea1a9
Patch0:		%{name}-pkgconfig.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
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
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_libdir}/libpixman-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpixman-1.so
%{_libdir}/libpixman-1.la
%{_includedir}/pixman-1
%{_pkgconfigdir}/pixman-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpixman-1.a

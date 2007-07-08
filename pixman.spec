%define	snap	20070625
Summary:	Biblioteka operacji na pikselach
Summary:	Pixel manipulation library
Name:		pixman
Version:	0.9.3
Release:	0.%{snap}.1
License:	BSD-like
Group:		Libraries
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	6e7e6d4c405a813d6e4e75364e3f2798
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libpixman
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
Obsoletes:	libpixman-devel

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
Obsoletes:	libpixman-static

%description static
This package contains static pixman library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki pixman.

%prep
%setup -q -n %{name}

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
%attr(755,root,root) %{_libdir}/libpixman.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpixman.so
%{_libdir}/libpixman.la
%{_includedir}/%{name}
%{_pkgconfigdir}/pixman.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpixman.a

#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	tests		# unit tests
%bcond_without	altivec		# PPC VMX/Altivec intrinsics
%bcond_without	armv6simd	# ARMv6 SIMD intrinsics
%bcond_without	armneon		# ARM Neon intrinsics
%bcond_without	arm64neon	# ARM64 Neon intrinsics
%bcond_without	loongson_mmi	# MIPS64 Loongson MMI intrinsics
%bcond_without	mips_dspr2	# MIPS32 DSPr2 intrinsics
%bcond_without	mmx		# x86 MMX instrinsics
%bcond_without	sse2		# x86 SSE2 instrinsics
%bcond_without	ssse3		# x86 SSSE3 instrinsics
%bcond_without	rvv		# RISC-V Vector extension

%ifnarch mips
%undefine	with_mips_dspr2
%endif
%ifnarch mips64
%undefine	with_loongson_mmi
%endif
%ifnarch %{ix86} %{x8664} x32
%undefine	with_mmx
%undefine	with_sse2
%undefine	with_ssse3
%endif
%ifnarch ppc ppc64
%undefine	with_altivec
%endif
%ifnarch %{arm}
%undefine	with_armv6simd
%undefine	with_armneon
%endif
%ifnarch aarch64
%undefine	with_arm64neon
%endif
%ifnarch riscv
%undefine	with_rvv
%endif
Summary:	Pixel manipulation library
Summary(pl.UTF-8):	Biblioteka operacji na pikselach
Name:		pixman
# 0.46.x is stable, 0.47.x unstable
Version:	0.46.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://www.cairographics.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	16fd88571a1cda22176bc82d653c6e85
URL:		https://pixman.org/
%if %{with sse2} || %{with ssse3}
BuildRequires:	gcc >= 6:4.2
%endif
%if %{with loongson_mmi}
BuildRequires:	gcc >= 6:4.4
%endif
%{?with_tests:BuildRequires:	libpng-devel}
BuildRequires:	meson >= 1.3.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
Obsoletes:	libic < 0.2
Obsoletes:	libpixman < 0.2
Obsoletes:	libpixregion < 0.2
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
Obsoletes:	libic-devel < 0.2
Obsoletes:	libpixman-devel < 0.2
Obsoletes:	libpixregion-devel < 0.2

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
Obsoletes:	libic-static < 0.2
Obsoletes:	libpixman-static < 0.2
Obsoletes:	libpixregion-static < 0.2

%description static
This package contains static pixman library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki pixman.

%prep
%setup -q

%{__sed} -i -e 's#<pixman-version.h>#"pixman-version.h"#' pixman/pixman.h

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Da64-neon=%{__enabled_disabled arm64neon} \
	-Darm-simd=%{__enabled_disabled arm-simd} \
	-Ddemos=disabled \
	-Dgnu-inline-asm=enabled \
	-Dgtk=disabled \
	-Dlibpng=enabled \
	-Dloongson-mmi=%{__enabled_disabled loongson_mmi} \
	-Dmips-dspr2=%{__enabled_disabled mips_dspr2} \
	-Dneon=%{__enabled_disabled armneon} \
	-Dopenmp=disabled \
	-Drvv=%{__enabled_disabled rvv} \
	-Dsse2=%{__enabled_disabled sse2} \
	-Dssse3=%{__enabled_disabled ssse3} \
	-Dtests=%{__enabled_disabled tests} \
	-Dtls=enabled \
	-Dvmx=%{__enabled_disabled altivec}

%meson_build

%if %{with tests}
%meson_test --no-rebuild --timeout-multiplier 2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%{_includedir}/pixman-1
%{_pkgconfigdir}/pixman-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpixman-1.a
%endif

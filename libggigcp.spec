%define major 1
%define libname %mklibname ggigcp %{major}
%define develname %mklibname ggigcp -d
%define staticname %mklibname ggigcp -d -s

Summary:	Extension to libggi for advanced color and palette handling
Name:		libggigcp
Version:	1.0.2
Release:	11
License:	Public Domain
Group:		System/Libraries
Url:		https://www.ggi-project.org/
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
BuildRequires:	libggi-devel	>= 2.2.2
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}

%description
It adds features for conversion between different color 
spaces such as RGBA, YUV, HSV and CMYK and some manipulation 
functions like brightness and color-blending.

%package -n %{libname}
Summary:	Main library for libggigcp
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Main library for libggigcp.

%package -n %{develname}
Summary:	Header files for libggigcp library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%mklibname ggigcp 1 -d

%description -n %{develname}
Header files for libggigcp library.

%package -n %{staticname}
Summary:	Static files for libggigcp library
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%mklibname ggigcp 1 -d -s

%description -n %{staticname}
Static files for libggigcp library.

%prep
%setup -q

%build
export echo=echo

%configure --enable-static

%make

%install
export echo=echo

%makeinstall_std

%ifarch x86_64
chrpath -d %{buildroot}%{_libdir}/ggi/gcp/default/color_gcp.so
%endif

%files
%doc README ChangeLog
%dir %{_libdir}/ggi/gcp
%dir %{_libdir}/ggi/gcp/default
%config(noreplace) %{_sysconfdir}/ggi/libggigcp.conf
%{_libdir}/ggi/gcp/default/*.so
%{_mandir}/man3/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc doc/*.txt doc/*.faq
%{_includedir}/ggi/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%{_mandir}/man7/*

%files -n %{staticname}
%{_libdir}/*.a

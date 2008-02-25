%define major 1
%define libname %mklibname ggigcp %{major}
%define develname %mklibname ggigcp -d
%define staticname %mklibname ggigcp -d -s

Summary:	Extension to libggi for advanced color and palette handling
Name:		libggigcp
Version:	1.0.2
Release:	%mkrel 3
License:	Public Domain
Group:		System/Libraries
Url:		http://www.ggi-project.org/
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
BuildRequires:	libggi-devel	>= 2.2.2
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname ggigcp 1 -d

%description -n %{develname}
Header files for libggigcp library.

%package -n %{staticname}
Summary:	Static files for libggigcp library
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}
Obsoletes:	%mklibname ggigcp 1 -d -s

%description -n %{staticname}
Static files for libggigcp library.

%prep
%setup -q
./autogen.sh

%build
export echo=echo

%configure2_5x --enable-static

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
export echo=echo

%makeinstall_std

%ifarch x86_64
chrpath -d %{buildroot}%{_libdir}/ggi/gcp/default/color_gcp.so
%endif

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%dir %{_libdir}/ggi/gcp
%dir %{_libdir}/ggi/gcp/default
%config(noreplace) %{_sysconfdir}/ggi/libggigcp.conf
%{_libdir}/ggi/gcp/default/*.la
%{_libdir}/ggi/gcp/default/*.so
%{_mandir}/man3/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/*.txt doc/*.faq
%{_includedir}/ggi/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man7/*

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/*.a

%define major 1
%define libname %mklibname ggigcp %{major}

Summary:	Extension to libggi for advanced color and palette handling
Name:		libggigcp
Version:	1.0.2
Release:	%mkrel 2
License:	Public Domain
Group:		System/Libraries
Url:		http://www.ggi-project.org/
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

%package -n %{libname}-devel
Summary:	Header files for libggigcp library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Header files for libggigcp library.

%package -n %{libname}-static-devel
Summary:	Static files for libggigcp library
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}

%description -n %{libname}-static-devel
Static files for libggigcp library.

%prep
%setup -q
./autogen.sh

%build
export echo=echo

%configure2_5x

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
%defattr(644,root,root,755)
%doc COPYING README ChangeLog
%dir %{_libdir}/ggi/gcp
%dir %{_libdir}/ggi/gcp/default
%attr(755,root,root)
%config(noreplace) %{_sysconfdir}/ggi/libggigcp.conf
%attr(755,root,root) %{_libdir}/ggi/gcp/default/*.la
%attr(755,root,root) %{_libdir}/ggi/gcp/default/*.so
%{_mandir}/man3/*

%files -n %{libname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(644,root,root,755)
%doc doc/*.txt doc/*.faq
%{_includedir}/ggi/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_mandir}/man7/*

%files -n %{libname}-static-devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/ggi/gcp/default/*.a



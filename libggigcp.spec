%define major 1
%define libname %mklibname ggigcp %{major}
%define develname %mklibname ggigcp -d
%define staticname %mklibname ggigcp -d -s

Summary:	Extension to libggi for advanced color and palette handling
Name:		libggigcp
Version:	1.0.2
Release:	9
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

%configure2_5x --enable-static

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-8mdv2011.0
+ Revision: 620123
- the mass rebuild of 2010.0 packages

* Sun Aug 02 2009 Funda Wang <fwang@mandriva.org> 1.0.2-7mdv2010.0
+ Revision: 407503
- fix requires

* Wed Mar 25 2009 Frederic Crozat <fcrozat@mandriva.com> 1.0.2-6mdv2009.1
+ Revision: 361069
- Fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 174779
- new devel library policy
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-2mdv2007.0
+ Revision: 125203
- fix dependencies

* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2007.1
+ Revision: 125109
- make it work
- remove rpath
- Import libggigcp


#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6A233DCD47A92289 (jmd@gnu.org)
#
Name     : ssw
Version  : 0.8
Release  : 4
URL      : https://alpha.gnu.org/gnu/ssw/spread-sheet-widget-0.8.tar.gz
Source0  : https://alpha.gnu.org/gnu/ssw/spread-sheet-widget-0.8.tar.gz
Source1  : https://alpha.gnu.org/gnu/ssw/spread-sheet-widget-0.8.tar.gz.sig
Summary  : A spreadsheet widget for Gtk+
Group    : Development/Tools
License  : GPL-3.0
Requires: ssw-info = %{version}-%{release}
Requires: ssw-lib = %{version}-%{release}
Requires: ssw-license = %{version}-%{release}
BuildRequires : pkgconfig(gtk+-3.0)

%description
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget for
viewing and manipulating 2 dimensional tabular data in a manner similar
to many popular spread sheet programs.

%package dev
Summary: dev components for the ssw package.
Group: Development
Requires: ssw-lib = %{version}-%{release}
Provides: ssw-devel = %{version}-%{release}
Requires: ssw = %{version}-%{release}

%description dev
dev components for the ssw package.


%package info
Summary: info components for the ssw package.
Group: Default

%description info
info components for the ssw package.


%package lib
Summary: lib components for the ssw package.
Group: Libraries
Requires: ssw-license = %{version}-%{release}

%description lib
lib components for the ssw package.


%package license
Summary: license components for the ssw package.
Group: Default

%description license
license components for the ssw package.


%prep
%setup -q -n spread-sheet-widget-0.8
cd %{_builddir}/spread-sheet-widget-0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652075900
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1652075900
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ssw
cp %{_builddir}/spread-sheet-widget-0.8/COPYING %{buildroot}/usr/share/package-licenses/ssw/569844e570df184cda2fa87c61168bd6ccd73499
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ssw-axis-model.h
/usr/include/ssw-sheet-axis.h
/usr/include/ssw-sheet.h
/usr/include/ssw-virtual-model.h
/usr/lib64/libspread-sheet-widget.so
/usr/lib64/pkgconfig/spread-sheet-widget.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/spread-sheet-widget.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libspread-sheet-widget.so.0
/usr/lib64/libspread-sheet-widget.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ssw/569844e570df184cda2fa87c61168bd6ccd73499

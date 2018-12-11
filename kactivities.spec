#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kactivities
Version  : 5.53.0
Release  : 9
URL      : https://download.kde.org/stable/frameworks/5.53/kactivities-5.53.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.53/kactivities-5.53.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.53/kactivities-5.53.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: kactivities-bin = %{version}-%{release}
Requires: kactivities-data = %{version}-%{release}
Requires: kactivities-lib = %{version}-%{release}
Requires: kactivities-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
In order to properly display the files, use the GNU man command.

%package bin
Summary: bin components for the kactivities package.
Group: Binaries
Requires: kactivities-data = %{version}-%{release}
Requires: kactivities-license = %{version}-%{release}

%description bin
bin components for the kactivities package.


%package data
Summary: data components for the kactivities package.
Group: Data

%description data
data components for the kactivities package.


%package dev
Summary: dev components for the kactivities package.
Group: Development
Requires: kactivities-lib = %{version}-%{release}
Requires: kactivities-bin = %{version}-%{release}
Requires: kactivities-data = %{version}-%{release}
Provides: kactivities-devel = %{version}-%{release}

%description dev
dev components for the kactivities package.


%package lib
Summary: lib components for the kactivities package.
Group: Libraries
Requires: kactivities-data = %{version}-%{release}
Requires: kactivities-license = %{version}-%{release}

%description lib
lib components for the kactivities package.


%package license
Summary: license components for the kactivities package.
Group: Default

%description license
license components for the kactivities package.


%prep
%setup -q -n kactivities-5.53.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544535407
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1544535407
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kactivities
cp COPYING %{buildroot}/usr/share/package-licenses/kactivities/COPYING
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/kactivities/COPYING.LGPL-2
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kactivities/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kactivities-cli

%files data
%defattr(-,root,root,-)
/usr/share/xdg/kactivities.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KActivities/KActivities/ActivitiesModel
/usr/include/KF5/KActivities/KActivities/Consumer
/usr/include/KF5/KActivities/KActivities/Controller
/usr/include/KF5/KActivities/KActivities/Info
/usr/include/KF5/KActivities/KActivities/ResourceInstance
/usr/include/KF5/KActivities/KActivities/Version
/usr/include/KF5/KActivities/kactivities/activitiesmodel.h
/usr/include/KF5/KActivities/kactivities/consumer.h
/usr/include/KF5/KActivities/kactivities/controller.h
/usr/include/KF5/KActivities/kactivities/info.h
/usr/include/KF5/KActivities/kactivities/kactivities_export.h
/usr/include/KF5/KActivities/kactivities/resourceinstance.h
/usr/include/KF5/KActivities/kactivities/version.h
/usr/include/KF5/kactivities_version.h
/usr/lib64/cmake/KF5Activities/KF5ActivitiesConfig.cmake
/usr/lib64/cmake/KF5Activities/KF5ActivitiesConfigVersion.cmake
/usr/lib64/cmake/KF5Activities/KF5ActivitiesLibraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Activities/KF5ActivitiesLibraryTargets.cmake
/usr/lib64/libKF5Activities.so
/usr/lib64/pkgconfig/libKActivities.pc
/usr/lib64/qt5/mkspecs/modules/qt_KActivities.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Activities.so.5
/usr/lib64/libKF5Activities.so.5.53.0
/usr/lib64/qt5/qml/org/kde/activities/libkactivitiesextensionplugin.so
/usr/lib64/qt5/qml/org/kde/activities/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kactivities/COPYING
/usr/share/package-licenses/kactivities/COPYING.LGPL-2
/usr/share/package-licenses/kactivities/COPYING.LIB

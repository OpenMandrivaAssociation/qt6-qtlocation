%define beta beta3
#define snapshot 20200627
%define major 6

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtlocation
Version:	6.10.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtlocation-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtlocation-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Qt %{major} Location module
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	%{_lib}Qt%{major}Core-devel
BuildRequires:	%{_lib}Qt%{major}Gui-devel
BuildRequires:	%{_lib}Qt%{major}Network-devel
BuildRequires:	%{_lib}Qt%{major}Xml-devel
BuildRequires:	%{_lib}Qt%{major}Widgets-devel
BuildRequires:	%{_lib}Qt%{major}SerialPort-devel = %{version}
BuildRequires:	%{_lib}Qt%{major}Sql-devel
BuildRequires:	%{_lib}Qt%{major}Positioning-devel
BuildRequires:	%{_lib}Qt%{major}PositioningQuick-devel
BuildRequires:	%{_lib}Qt%{major}PrintSupport-devel
BuildRequires:	%{_lib}Qt%{major}OpenGL-devel
BuildRequires:	%{_lib}Qt%{major}OpenGLWidgets-devel
BuildRequires:	%{_lib}Qt%{major}DBus-devel
BuildRequires:	qt%{major}-cmake
BuildRequires:	cmake(Qt%{major}Quick)
BuildRequires:	cmake(Qt%{major}Qml)
BuildRequires:	cmake(Qt%{major}QmlModels)
BuildRequires:	cmake(Qt%{major}Test)
BuildRequires:	cmake(Qt%{major}QuickTest)
BuildRequires:	cmake(Qt%{major}QuickShapesPrivate)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(gypsy)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(geoclue-2.0)
BuildRequires:	cmake(LLVM)
BuildRequires:	cmake(Clang)
# Not really required, but referenced by LLVMExports.cmake
# (and then required because of the integrity check)
BuildRequires:	%{_lib}gpuruntime
License:	LGPLv3/GPLv3/GPLv2

%description
Qt %{major} Location module

%global extra_files_Location \
%{_qtdir}/qml/QtLocation \
%{_qtdir}/plugins/geoservices

%global extra_devel_files_Location \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6declarative_location*.cmake \
%{_qtdir}/sbom/*

%global extra_devel_reqprov_Location \
Requires: cmake(Qt%{major}QuickShapesPrivate)

%qt6libs Location

%package examples
Summary:	Example code demonstrating the use of %{name}
Group:		Development/KDE and Qt

%description examples
Example code demonstrating the use of %{name}

%files examples
%{_qtdir}/examples/location

%prep
%autosetup -p1 -n qtlocation%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON

%build
%ninja_build -C build

%install
%ninja_install -C build
%qt6_postinstall

Name:           ros-hydro-naoqi-tools
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS naoqi_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/nao_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-nao-description
Requires:       ros-hydro-romeo-description
BuildRequires:  ros-hydro-catkin

%description
Set of tools provided by Aldebaran to convert Aldebaran files (URDF, blender...)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Nov 26 2014 Mikael Arguedas <mikael.arguedas@gmail.com> - 0.4.2-0
- Autogenerated by Bloom


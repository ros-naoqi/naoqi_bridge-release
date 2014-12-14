Name:           ros-hydro-naoqi-msgs
Version:        0.4.3
Release:        0%{?dist}
Summary:        ROS naoqi_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nao_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib-msgs
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-trajectory-msgs
BuildRequires:  ros-hydro-actionlib-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-trajectory-msgs
Conflicts:      ros-hydro-nao-msgs

%description
Message and service declarations for the Nao humanoid

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Dec 14 2014 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.3-0
- Autogenerated by Bloom

* Wed Nov 26 2014 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.2-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.1-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Severin Lemaignan <severin.lemaignan@epfl.ch> - 0.4.0-0
- Autogenerated by Bloom


%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-usb-cam-controllers
Version:        0.2.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS usb_cam_controllers package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-camera-info-manager
Requires:       ros-noetic-controller-interface
Requires:       ros-noetic-controller-manager
Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-image-transport
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-usb-cam-hardware-interface
BuildRequires:  ros-noetic-camera-info-manager
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-controller-interface
BuildRequires:  ros-noetic-controller-manager
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-image-transport
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-usb-cam-hardware-interface
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The usb_cam_controllers package

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Jul 10 2020 Yoshito Okada <yoshito@todo.todo> - 0.2.1-1
- Autogenerated by Bloom

* Sat Jun 27 2020 Yoshito Okada <yoshito@todo.todo> - 0.0.5-1
- Autogenerated by Bloom


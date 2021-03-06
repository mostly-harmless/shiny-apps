Name: shinyapps

# Specify dynamic version with: --define "version 1.2.3"
Version:	%{version}
Release:	%{release}
Summary:	Shiny Apps

Group:		Web/Applications
License:	BSD
URL:		http://snap.uaf.edu:8080
Source0:	shinyapps.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: 	noarch
ExclusiveArch:  noarch

%define inst_dir /var/www/shiny-server
%define hostname www.snap.uaf.edu

%description
This package contains the various R Shiny apps developed for the SNAP website.

%prep
%setup -c

%build

%install
rm -rf ${RPM_BUILD_ROOT}

mkdir -p ${RPM_BUILD_ROOT}/%{inst_dir}
mkdir -p ${RPM_BUILD_ROOT}/home/jenkins/
mkdir -p ${RPM_BUILD_ROOT}/tmp

cp -aR * ${RPM_BUILD_ROOT}/%{inst_dir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{inst_dir}/*
%exclude %{inst_dir}/build
%exclude %{inst_dir}/README.md
%ghost %attr(644,jenkins,jenkins) /var/log/httpd/shinyapps-update_log

%post
/usr/local/bin/shiny-server

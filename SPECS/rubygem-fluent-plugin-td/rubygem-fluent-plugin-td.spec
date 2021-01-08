%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name fluent-plugin-td

Name:           rubygem-fluent-plugin-td
Version:        1.1.0
Release:        1%{?dist}
Summary:        Fluentd plugin for Treasure Data Service
Group:          Development/Languages
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRequires:  ruby > 2.1.0
Requires:       rubygem-fluentd
Requires:       rubygem-td-client

%description
This Fluentd output plugin is used to upload 
logs to Treasure Data using Treasure Data's REST APIs.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Mon Jan 04 2021 Henry Li <lihl@microsoft.com> 1.1.0-1
-   Original version for CBL-Mariner.
-   License verified.

%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name td-client

Name:           rubygem-td-client
Version:        1.0.7
Release:        1%{?dist}
Summary:        Ruby Client Library for Treasure Data
Group:          Development/Languages
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRequires:  ruby >= 2.1.0
Requires:       rubygem-msgpack >= 0.5.6
Requires:       rubygem-msgpack < 2
Requires:       rubygem-httpclient >= 2.7

%description
Ruby Client Library for Treasure Data.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Mon Jan 04 2021 Henry Li <lihl@microsoft.com> 1.0.7-1
-   Original version for CBL-Mariner.
-   License verified.

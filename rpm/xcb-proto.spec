Name:       xcb-proto
Version:    1.17.0
Release:    1%{?dist}
Summary:    XML-XCB protocol descriptions used by libxcb for the X11 protocol & extensions
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/proto/xcbproto
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
Requires:   python3-base
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  python3-base
BuildRequires:  python3-rpm-macros

%description
Base package for %{name}.

%package devel
Summary:    XML-XCB protocol descriptions used by libxcb for the X11 protocol & extensions

%description devel
xcb-proto provides the XML-XCB protocol descriptions that libxcb uses
to generate the majority of its code and API. We provide them
separately from libxcb to allow reuse by other projects, such as
additional language bindings, protocol dissectors, or documentation
generators.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files devel
%license COPYING
%{_datadir}/xcb
%{_datadir}/pkgconfig/%{name}.pc
%{python3_sitelib}/xcbgen

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-man-pages
Version  : 6
Release  : 2
URL      : https://github.com/clearlinux/clr-man-pages/releases/download/v6/clr-man-pages-6.tar.xz
Source0  : https://github.com/clearlinux/clr-man-pages/releases/download/v6/clr-man-pages-6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-SA-3.0
Requires: clr-man-pages-doc

%description
## clr-man-pages
Provides a few extra man pages that describes the particularities
of Clear Linux OS for Intel Architecture, and some useful tips
and tricks for the most frequently asked questions.

%package doc
Summary: doc components for the clr-man-pages package.
Group: Documentation

%description doc
doc components for the clr-man-pages package.


%prep
%setup -q -n clr-man-pages-6

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485795946
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1485795946
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras_Preprocessing
Version  : 1.1.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/6d/2b/d45a295e6b31d8b6663b705dff2f178ae16e8d2eac41097810a411d7b10f/Keras_Preprocessing-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/2b/d45a295e6b31d8b6663b705dff2f178ae16e8d2eac41097810a411d7b10f/Keras_Preprocessing-1.1.0.tar.gz
Summary  : Easy data preprocessing and data augmentation for deep learning models
Group    : Development/Tools
License  : MIT
Requires: Keras_Preprocessing-license = %{version}-%{release}
Requires: Keras_Preprocessing-python = %{version}-%{release}
Requires: Keras_Preprocessing-python3 = %{version}-%{release}
Requires: Keras
Requires: Pillow
Requires: flake8
Requires: numpy
Requires: pandas
Requires: scipy
Requires: six
Requires: tensorflow
BuildRequires : Keras
BuildRequires : Pillow
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : scipy
BuildRequires : six
BuildRequires : tensorflow

%description
# Keras Preprocessing
[![Build Status](https://travis-ci.org/keras-team/keras-preprocessing.svg?branch=master)](https://travis-ci.org/keras-team/keras-preprocessing)

%package license
Summary: license components for the Keras_Preprocessing package.
Group: Default

%description license
license components for the Keras_Preprocessing package.


%package python
Summary: python components for the Keras_Preprocessing package.
Group: Default
Requires: Keras_Preprocessing-python3 = %{version}-%{release}
Provides: keras_preprocessing-python

%description python
python components for the Keras_Preprocessing package.


%package python3
Summary: python3 components for the Keras_Preprocessing package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Keras_Preprocessing package.


%prep
%setup -q -n Keras_Preprocessing-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559408261
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Keras_Preprocessing
cp LICENSE %{buildroot}/usr/share/package-licenses/Keras_Preprocessing/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Keras_Preprocessing/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

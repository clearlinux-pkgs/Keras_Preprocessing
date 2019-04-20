#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras_Preprocessing
Version  : 1.0.9
Release  : 19
URL      : https://files.pythonhosted.org/packages/59/ed/0119d5a5d02731f8532544dc341bb07a2ab9a0e9873ad6051a180f7076e2/Keras_Preprocessing-1.0.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/59/ed/0119d5a5d02731f8532544dc341bb07a2ab9a0e9873ad6051a180f7076e2/Keras_Preprocessing-1.0.9.tar.gz
Summary  : Easy data preprocessing and data augmentation for deep learning models
Group    : Development/Tools
License  : MIT
Requires: Keras_Preprocessing-license = %{version}-%{release}
Requires: Keras_Preprocessing-python = %{version}-%{release}
Requires: Keras_Preprocessing-python3 = %{version}-%{release}
Requires: Pillow
Requires: flake8
Requires: numpy
Requires: pandas
Requires: scipy
Requires: six
Requires: tensorflow
BuildRequires : Keras
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : six

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
%setup -q -n Keras_Preprocessing-1.0.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549461879
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
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

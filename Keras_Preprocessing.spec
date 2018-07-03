#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras_Preprocessing
Version  : 1.0.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/b2/f6/375a3648d3cae006b1a08ebd9b9614c1c4b372cce54d11e5870adc45ec19/Keras_Preprocessing-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b2/f6/375a3648d3cae006b1a08ebd9b9614c1c4b372cce54d11e5870adc45ec19/Keras_Preprocessing-1.0.1.tar.gz
Summary  : Easy data preprocessing and data augmentation for deep learning models
Group    : Development/Tools
License  : MIT
Requires: Keras_Preprocessing-python3
Requires: Keras_Preprocessing-python
Requires: numpy
Requires: scipy
Requires: six
BuildRequires : Keras
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : setuptools
BuildRequires : six

%description
Keras Preprocessing is the data preprocessing
        and data augmentation module of the Keras deep learning library.
        It provides utilities for working with image data, text data,
        and sequence data.

%package python
Summary: python components for the Keras_Preprocessing package.
Group: Default
Requires: Keras_Preprocessing-python3
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
%setup -q -n Keras_Preprocessing-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528565938
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

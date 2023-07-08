

def decode(stream, **kwargs):
    """Return the decoded JPEG data from `stream` as a
    :class:`numpy.ndarray`.

    +++ 1.0

    Parameters
    ----------
    stream : str, pathlib.Path, bytes or file-like
        The path to the JPEG file or a Python object containing the
        encoded JPEG data. If using a file-like then the object must have
        ``tell()``, ``seek()`` and ``read()`` methods.

    Returns
    -------
    numpy.ndarray
        An array of containing the decoded image data.

    Raises
    ------
    RuntimeError
        If the decoding failed.
    """
    raise NotImplementedError("pylibjpeg_turbo is a work-in-progress")

def decode_pixel_data(stream, ds=None, **kwargs):
    """Return the decoded JPEG data as a :class:`numpy.ndarray`.

    Intended for use with *pydicom* ``Dataset`` objects.

    Parameters
    ----------
    stream : bytes or file-like
        A Python object containing the encoded JPEG data. If not
        :class:`bytes` then the object must have ``tell()``, ``seek()`` and
        ``read()`` methods.
    ds : pydicom.dataset.Dataset, optional
        A :class:`~pydicom.dataset.Dataset` containing the group ``0x0028``
        elements corresponding to the *Pixel data*. If used then the
        *Samples per Pixel*, *Bits Stored* and *Pixel Representation* values
        will be checked against the JPEG data and warnings issued if
        different.

    Returns
    -------
    numpy.ndarray
        A 1D array of ``numpy.uint8`` containing the decoded image data.

    Raises
    ------
    RuntimeError
        If the decoding failed.
    """
    raise NotImplementedError("pylibjpeg_turbo pixel decoding is a work-in-progress")
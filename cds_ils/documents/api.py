# SPDX-FileCopyrightText: 2026 CERN.
# SPDX-License-Identifier: MIT

"""CDS-ILS Document APIs."""

from invenio_app_ils.documents.api import Document as ILSDocument

class Document(ILSDocument):
    """CDS-ILS Document record class."""

    DOCUMENT_TYPES = ILSDocument.DOCUMENT_TYPES + ["THESIS"]
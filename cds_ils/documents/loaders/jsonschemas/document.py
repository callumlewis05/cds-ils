# SPDX-FileCopyrightText: 2026 CERN.
# SPDX-License-Identifier: MIT

"""Document schema for overwritten marshmallow loader with new document type."""

from marshmallow import fields, validate

from invenio_app_ils.documents.loaders.jsonschemas.document import (
    DocumentSchemaV1 as ILSDocumentSchemaV1,
)

from cds_ils.documents.api import Document


class DocumentSchemaV1(ILSDocumentSchemaV1):
    """CDS-ILS Document schema."""

    document_type = fields.Str(
        required=True, validate=validate.OneOf(Document.DOCUMENT_TYPES)
    )
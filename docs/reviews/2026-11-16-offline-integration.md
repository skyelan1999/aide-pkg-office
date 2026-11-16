# Office 1.3.0: built-in offline integration

Office 1.3.0 removes the external Collabora service settings. The complete Aide
runtime bundles a pinned, unmodified CODE engine and manages it automatically.
Opening, editing and saving documents requires no Office addresses, extra
service deployment or runtime downloads. The Node adapter alone cannot perform
Office operations; the complete host must provide `office-offline-v1`.

The engine and WOPI callback listen only on loopback inside Aide. Browser/editor
traffic uses an Aide-issued document-session capability on the existing Aide
origin. Public WOPI, general document read/edit HTTP entry points, administration
and conversion services are refused. AI operations remain internal native Aide
tool calls, with task/workspace/sandbox, visibility and stale-write checks.
The child does not inherit provider credentials or proxy environment variables.

The six tool names and input contracts are retained. Old service settings may
remain in preserved user data but are ignored by the new host; they are not
shown as required settings. Human preview does not block AI writes; active
editing or a pending save protects the document until inactivity and confirmed
save. Documents and user settings are not migration inputs for this package.

Isolated Linux ARM64 acceptance observed actual DOCX/XLSX/PPTX preview/edit/save
and disk readback with external networking unavailable and no browser external
requests. A fresh host with no Office settings also rendered Chinese DOCX text.
Pinned ARM64/AMD64 archive/executable integrity and offline staging were checked;
AMD64 execution, native Windows/macOS, SSH and enterprise capacity were not
accepted. No paid model inference or Collabora subscription is included. Cloud
model inference still needs its configured provider; offline inference requires
an already available local model.

Completed source and host functional checks are recorded in
`docs/release-verification-1.3.0.json`. Publication additionally requires the host
full gate and acceptance of the exact final ZIP; their receipts are linked from
the host PR, tracking issue and Release. Keeping the package digest outside this
ZIP avoids a self-referential checksum. Host change and tracking:

- https://github.com/skyelan1999/aide/pull/938
- https://github.com/skyelan1999/aide/issues/937

The adapter is MIT licensed. The engine is part of the Aide runtime, not this
ZIP, and retains MPL and included third-party notices. Its source version and
digests are pinned in the host's `docker/office-engine/source.json`. This package
does not bundle enterprise support or an SLA.

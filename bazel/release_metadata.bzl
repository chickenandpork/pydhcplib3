def _release_metadata_impl(repository_ctx):
    manifest = json.decode(
        repository_ctx.read(repository_ctx.attr.manifest),
    )

    project_name = repository_ctx.attr.project_name
    version = manifest["."]

    repository_ctx.file(
        "metadata.bzl",
        """
PROJECT_NAME = {project_name}
VERSION = {version}
DIST_NAME = {dist_name}
""".format(
            project_name = repr(project_name),
            version = repr(version),
            dist_name = repr(project_name + "-" + version),
        ),
    )

    repository_ctx.file(
        "BUILD.bazel",
        'exports_files(["metadata.bzl"])\n',
    )

release_metadata = repository_rule(
    implementation = _release_metadata_impl,
    attrs = {
        "manifest": attr.label(allow_single_file = True, mandatory = True),
        "project_name": attr.string(mandatory = True),
    },
)

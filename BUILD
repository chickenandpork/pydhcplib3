load("@release_metadata//:metadata.bzl", "DIST_NAME")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")

pkg_tar(
    name = "source_tar",
    srcs = [":source_dist"],
    package_dir = DIST_NAME,
    extension = "tar",
)

genrule(
    name = "source_tar_zst",
    srcs = [":source_tar"],
    outs = [DIST_NAME + ".tar.zst"],
    tags = [ "release-artifact" ],
    tools = ["@zstd//:zstd_cli"],
    cmd = """$(execpath @zstd//:zstd_cli) -19 -T1 -f $(execpath :source_tar) -o $@""",
)

filegroup(
    name = "source_dist",
    srcs = glob(
        ["**"],
        exclude = [
            ".git/**",
            "bazel-*/**",
        ],
    ),
    visibility = ["//visibility:public"],
)

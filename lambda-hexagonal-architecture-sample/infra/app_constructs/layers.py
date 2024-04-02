from typing import List, Optional

from aws_cdk import Stack
from aws_cdk import aws_lambda as lambda_
from constructs import Construct

class SharedLayer(Construct):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        compatible_runtimes: List[lambda_.Runtime],
        entry: str,
        layer_version_name: str,
    ) -> None:
        super().__init__(scope, construct_id)

        self._libraries_layer = lambda_.LayerVersion(
            self,
            "SimpleCrudAppLayers",
            layer_version_name=layer_version_name,
            code=lambda_.Code.from_asset(entry),
            compatible_runtimes=compatible_runtimes,
            # 注意：这里没有 `bundling` 选项，依赖需要手动打包或使用工具处理
        )

    @property
    def libraries_layer(self):
        return self._libraries_layer

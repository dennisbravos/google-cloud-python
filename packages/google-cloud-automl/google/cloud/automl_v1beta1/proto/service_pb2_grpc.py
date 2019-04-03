# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.automl_v1beta1.proto import (
    column_spec_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    dataset_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    model_evaluation_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_model__evaluation__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    model_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_model__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    service_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    table_spec_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_table__spec__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class AutoMlStub(object):
    """AutoML Server API.

  The resource names are assigned by the server.
  The server never reuses names that it has created after the resources with
  those names are deleted.

  An ID of a resource is the last element of the item's resource name. For
  `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then
  the id for the item is `{dataset_id}`.

  Currently the only supported `location_id` is "us-central1".

  On any input that is documented to expect a string parameter in
  snake_case or kebab-case, either of those cases is accepted.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateDataset = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/CreateDataset",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.CreateDatasetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2.Dataset.FromString,
        )
        self.GetDataset = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/GetDataset",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetDatasetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2.Dataset.FromString,
        )
        self.ListDatasets = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ListDatasets",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListDatasetsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListDatasetsResponse.FromString,
        )
        self.UpdateDataset = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/UpdateDataset",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.UpdateDatasetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2.Dataset.FromString,
        )
        self.DeleteDataset = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/DeleteDataset",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.DeleteDatasetRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ImportData = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ImportData",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ImportDataRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ExportData = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ExportData",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ExportDataRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetAnnotationSpec = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/GetAnnotationSpec",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetAnnotationSpecRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2.AnnotationSpec.FromString,
        )
        self.GetTableSpec = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/GetTableSpec",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetTableSpecRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_table__spec__pb2.TableSpec.FromString,
        )
        self.ListTableSpecs = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ListTableSpecs",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListTableSpecsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListTableSpecsResponse.FromString,
        )
        self.UpdateTableSpec = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/UpdateTableSpec",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.UpdateTableSpecRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_table__spec__pb2.TableSpec.FromString,
        )
        self.GetColumnSpec = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/GetColumnSpec",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetColumnSpecRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2.ColumnSpec.FromString,
        )
        self.ListColumnSpecs = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ListColumnSpecs",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListColumnSpecsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListColumnSpecsResponse.FromString,
        )
        self.UpdateColumnSpec = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/UpdateColumnSpec",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.UpdateColumnSpecRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2.ColumnSpec.FromString,
        )
        self.CreateModel = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/CreateModel",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.CreateModelRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetModel = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/GetModel",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetModelRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_model__pb2.Model.FromString,
        )
        self.ListModels = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ListModels",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListModelsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListModelsResponse.FromString,
        )
        self.DeleteModel = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/DeleteModel",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.DeleteModelRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.DeployModel = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/DeployModel",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.DeployModelRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.UndeployModel = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/UndeployModel",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.UndeployModelRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ExportModel = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ExportModel",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ExportModelRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.ExportEvaluatedExamples = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ExportEvaluatedExamples",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ExportEvaluatedExamplesRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.GetModelEvaluation = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/GetModelEvaluation",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetModelEvaluationRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_model__evaluation__pb2.ModelEvaluation.FromString,
        )
        self.ListModelEvaluations = channel.unary_unary(
            "/google.cloud.automl.v1beta1.AutoMl/ListModelEvaluations",
            request_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListModelEvaluationsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListModelEvaluationsResponse.FromString,
        )


class AutoMlServicer(object):
    """AutoML Server API.

  The resource names are assigned by the server.
  The server never reuses names that it has created after the resources with
  those names are deleted.

  An ID of a resource is the last element of the item's resource name. For
  `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then
  the id for the item is `{dataset_id}`.

  Currently the only supported `location_id` is "us-central1".

  On any input that is documented to expect a string parameter in
  snake_case or kebab-case, either of those cases is accepted.
  """

    def CreateDataset(self, request, context):
        """Creates a dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetDataset(self, request, context):
        """Gets a dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListDatasets(self, request, context):
        """Lists datasets in a project.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateDataset(self, request, context):
        """Updates a dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteDataset(self, request, context):
        """Deletes a dataset and all of its contents.
    Returns empty response in the
    [response][google.longrunning.Operation.response] field when it completes,
    and `delete_details` in the
    [metadata][google.longrunning.Operation.metadata] field.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ImportData(self, request, context):
        """Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

    For Tables:
    *   A
    [schema_inference_version][google.cloud.automl.v1beta1.InputConfig.params]
    parameter must be explicitly set.
    Returns an empty response in the
    [response][google.longrunning.Operation.response] field when it completes.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExportData(self, request, context):
        """Exports dataset's data to the provided output location.
    Returns an empty response in the
    [response][google.longrunning.Operation.response] field when it completes.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetAnnotationSpec(self, request, context):
        """Gets an annotation spec.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTableSpec(self, request, context):
        """Gets a table spec.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListTableSpecs(self, request, context):
        """Lists table specs in a dataset.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateTableSpec(self, request, context):
        """Updates a table spec.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetColumnSpec(self, request, context):
        """Gets a column spec.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListColumnSpecs(self, request, context):
        """Lists column specs in a table spec.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateColumnSpec(self, request, context):
        """Updates a column spec.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateModel(self, request, context):
        """Creates a model.
    Returns a Model in the [response][google.longrunning.Operation.response]
    field when it completes.
    When you create a model, several model evaluations are created for it:
    a global evaluation, and one evaluation for each annotation spec.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetModel(self, request, context):
        """Gets a model.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListModels(self, request, context):
        """Lists models.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteModel(self, request, context):
        """Deletes a model.
    Returns `google.protobuf.Empty` in the
    [response][google.longrunning.Operation.response] field when it completes,
    and `delete_details` in the
    [metadata][google.longrunning.Operation.metadata] field.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeployModel(self, request, context):
        """Deploys a model. If a model is already deployed, deploying it with the
    same parameters has no effect. Deploying with different parametrs
    (as e.g. changing

    [node_number][google.cloud.automl.v1beta1.ImageObjectDetectionModelDeploymentMetadata.node_number]
    ) will update the deployment without pausing the model's availability.

    Only applicable for Text Classification, Image Object Detection and Tables;
    all other domains manage deployment automatically.

    Returns an empty response in the
    [response][google.longrunning.Operation.response] field when it completes.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UndeployModel(self, request, context):
        """Undeploys a model. If the model is not deployed this method has no effect.

    Only applicable for Text Classification, Image Object Detection and Tables;
    all other domains manage deployment automatically.

    Returns an empty response in the
    [response][google.longrunning.Operation.response] field when it completes.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExportModel(self, request, context):
        """Exports a trained, "export-able", model to a user specified Google Cloud
    Storage location. A model is considered export-able if and only if it has
    an export format defined for it in

    [ModelExportOutputConfig][google.cloud.automl.v1beta1.ModelExportOutputConfig].

    Returns an empty response in the
    [response][google.longrunning.Operation.response] field when it completes.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExportEvaluatedExamples(self, request, context):
        """Exports examples on which the model was evaluated (i.e. which were in the
    TEST set of the dataset the model was created from), together with their
    ground truth annotations and the annotations created (predicted) by the
    model.
    The examples, ground truth and predictions are exported in the state
    they were at the moment the model was evaluated.

    This export is available only for 30 days since the model evaluation is
    created.

    Currently only available for Tables.

    Returns an empty response in the
    [response][google.longrunning.Operation.response] field when it completes.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetModelEvaluation(self, request, context):
        """Gets a model evaluation.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListModelEvaluations(self, request, context):
        """Lists model evaluations.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AutoMlServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateDataset": grpc.unary_unary_rpc_method_handler(
            servicer.CreateDataset,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.CreateDatasetRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2.Dataset.SerializeToString,
        ),
        "GetDataset": grpc.unary_unary_rpc_method_handler(
            servicer.GetDataset,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetDatasetRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2.Dataset.SerializeToString,
        ),
        "ListDatasets": grpc.unary_unary_rpc_method_handler(
            servicer.ListDatasets,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListDatasetsRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListDatasetsResponse.SerializeToString,
        ),
        "UpdateDataset": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateDataset,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.UpdateDatasetRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2.Dataset.SerializeToString,
        ),
        "DeleteDataset": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteDataset,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.DeleteDatasetRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ImportData": grpc.unary_unary_rpc_method_handler(
            servicer.ImportData,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ImportDataRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ExportData": grpc.unary_unary_rpc_method_handler(
            servicer.ExportData,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ExportDataRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetAnnotationSpec": grpc.unary_unary_rpc_method_handler(
            servicer.GetAnnotationSpec,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetAnnotationSpecRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_dataset__pb2.AnnotationSpec.SerializeToString,
        ),
        "GetTableSpec": grpc.unary_unary_rpc_method_handler(
            servicer.GetTableSpec,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetTableSpecRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_table__spec__pb2.TableSpec.SerializeToString,
        ),
        "ListTableSpecs": grpc.unary_unary_rpc_method_handler(
            servicer.ListTableSpecs,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListTableSpecsRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListTableSpecsResponse.SerializeToString,
        ),
        "UpdateTableSpec": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateTableSpec,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.UpdateTableSpecRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_table__spec__pb2.TableSpec.SerializeToString,
        ),
        "GetColumnSpec": grpc.unary_unary_rpc_method_handler(
            servicer.GetColumnSpec,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetColumnSpecRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2.ColumnSpec.SerializeToString,
        ),
        "ListColumnSpecs": grpc.unary_unary_rpc_method_handler(
            servicer.ListColumnSpecs,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListColumnSpecsRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListColumnSpecsResponse.SerializeToString,
        ),
        "UpdateColumnSpec": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateColumnSpec,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.UpdateColumnSpecRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2.ColumnSpec.SerializeToString,
        ),
        "CreateModel": grpc.unary_unary_rpc_method_handler(
            servicer.CreateModel,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.CreateModelRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetModel": grpc.unary_unary_rpc_method_handler(
            servicer.GetModel,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetModelRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_model__pb2.Model.SerializeToString,
        ),
        "ListModels": grpc.unary_unary_rpc_method_handler(
            servicer.ListModels,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListModelsRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListModelsResponse.SerializeToString,
        ),
        "DeleteModel": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteModel,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.DeleteModelRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "DeployModel": grpc.unary_unary_rpc_method_handler(
            servicer.DeployModel,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.DeployModelRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "UndeployModel": grpc.unary_unary_rpc_method_handler(
            servicer.UndeployModel,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.UndeployModelRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ExportModel": grpc.unary_unary_rpc_method_handler(
            servicer.ExportModel,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ExportModelRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "ExportEvaluatedExamples": grpc.unary_unary_rpc_method_handler(
            servicer.ExportEvaluatedExamples,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ExportEvaluatedExamplesRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "GetModelEvaluation": grpc.unary_unary_rpc_method_handler(
            servicer.GetModelEvaluation,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.GetModelEvaluationRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_model__evaluation__pb2.ModelEvaluation.SerializeToString,
        ),
        "ListModelEvaluations": grpc.unary_unary_rpc_method_handler(
            servicer.ListModelEvaluations,
            request_deserializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListModelEvaluationsRequest.FromString,
            response_serializer=google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_service__pb2.ListModelEvaluationsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.automl.v1beta1.AutoMl", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))

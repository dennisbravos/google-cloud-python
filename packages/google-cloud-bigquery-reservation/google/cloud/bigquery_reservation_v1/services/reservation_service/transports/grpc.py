# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import gapic_v1  # type: ignore
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.bigquery_reservation_v1.types import reservation
from google.cloud.bigquery_reservation_v1.types import reservation as gcbr_reservation
from google.protobuf import empty_pb2  # type: ignore
from .base import ReservationServiceTransport, DEFAULT_CLIENT_INFO


class ReservationServiceGrpcTransport(ReservationServiceTransport):
    """gRPC backend transport for ReservationService.

    This API allows users to manage their flat-rate BigQuery
    reservations.

    A reservation provides computational resource guarantees, in the
    form of `slots <https://cloud.google.com/bigquery/docs/slots>`__, to
    users. A slot is a unit of computational power in BigQuery, and
    serves as the basic unit of parallelism. In a scan of a
    multi-partitioned table, a single slot operates on a single
    partition of the table. A reservation resource exists as a child
    resource of the admin project and location, e.g.:
    ``projects/myproject/locations/US/reservations/reservationName``.

    A capacity commitment is a way to purchase compute capacity for
    BigQuery jobs (in the form of slots) with some committed period of
    usage. A capacity commitment resource exists as a child resource of
    the admin project and location, e.g.:
    ``projects/myproject/locations/US/capacityCommitments/id``.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "bigqueryreservation.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "bigqueryreservation.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def create_reservation(
        self,
    ) -> Callable[
        [gcbr_reservation.CreateReservationRequest], gcbr_reservation.Reservation
    ]:
        r"""Return a callable for the create reservation method over gRPC.

        Creates a new reservation resource.

        Returns:
            Callable[[~.CreateReservationRequest],
                    ~.Reservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_reservation" not in self._stubs:
            self._stubs["create_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateReservation",
                request_serializer=gcbr_reservation.CreateReservationRequest.serialize,
                response_deserializer=gcbr_reservation.Reservation.deserialize,
            )
        return self._stubs["create_reservation"]

    @property
    def list_reservations(
        self,
    ) -> Callable[
        [reservation.ListReservationsRequest], reservation.ListReservationsResponse
    ]:
        r"""Return a callable for the list reservations method over gRPC.

        Lists all the reservations for the project in the
        specified location.

        Returns:
            Callable[[~.ListReservationsRequest],
                    ~.ListReservationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_reservations" not in self._stubs:
            self._stubs["list_reservations"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListReservations",
                request_serializer=reservation.ListReservationsRequest.serialize,
                response_deserializer=reservation.ListReservationsResponse.deserialize,
            )
        return self._stubs["list_reservations"]

    @property
    def get_reservation(
        self,
    ) -> Callable[[reservation.GetReservationRequest], reservation.Reservation]:
        r"""Return a callable for the get reservation method over gRPC.

        Returns information about the reservation.

        Returns:
            Callable[[~.GetReservationRequest],
                    ~.Reservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_reservation" not in self._stubs:
            self._stubs["get_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetReservation",
                request_serializer=reservation.GetReservationRequest.serialize,
                response_deserializer=reservation.Reservation.deserialize,
            )
        return self._stubs["get_reservation"]

    @property
    def delete_reservation(
        self,
    ) -> Callable[[reservation.DeleteReservationRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete reservation method over gRPC.

        Deletes a reservation. Returns
        ``google.rpc.Code.FAILED_PRECONDITION`` when reservation has
        assignments.

        Returns:
            Callable[[~.DeleteReservationRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_reservation" not in self._stubs:
            self._stubs["delete_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteReservation",
                request_serializer=reservation.DeleteReservationRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_reservation"]

    @property
    def update_reservation(
        self,
    ) -> Callable[
        [gcbr_reservation.UpdateReservationRequest], gcbr_reservation.Reservation
    ]:
        r"""Return a callable for the update reservation method over gRPC.

        Updates an existing reservation resource.

        Returns:
            Callable[[~.UpdateReservationRequest],
                    ~.Reservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_reservation" not in self._stubs:
            self._stubs["update_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateReservation",
                request_serializer=gcbr_reservation.UpdateReservationRequest.serialize,
                response_deserializer=gcbr_reservation.Reservation.deserialize,
            )
        return self._stubs["update_reservation"]

    @property
    def create_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.CreateCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        r"""Return a callable for the create capacity commitment method over gRPC.

        Creates a new capacity commitment resource.

        Returns:
            Callable[[~.CreateCapacityCommitmentRequest],
                    ~.CapacityCommitment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_capacity_commitment" not in self._stubs:
            self._stubs["create_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateCapacityCommitment",
                request_serializer=reservation.CreateCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["create_capacity_commitment"]

    @property
    def list_capacity_commitments(
        self,
    ) -> Callable[
        [reservation.ListCapacityCommitmentsRequest],
        reservation.ListCapacityCommitmentsResponse,
    ]:
        r"""Return a callable for the list capacity commitments method over gRPC.

        Lists all the capacity commitments for the admin
        project.

        Returns:
            Callable[[~.ListCapacityCommitmentsRequest],
                    ~.ListCapacityCommitmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_capacity_commitments" not in self._stubs:
            self._stubs["list_capacity_commitments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListCapacityCommitments",
                request_serializer=reservation.ListCapacityCommitmentsRequest.serialize,
                response_deserializer=reservation.ListCapacityCommitmentsResponse.deserialize,
            )
        return self._stubs["list_capacity_commitments"]

    @property
    def get_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.GetCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        r"""Return a callable for the get capacity commitment method over gRPC.

        Returns information about the capacity commitment.

        Returns:
            Callable[[~.GetCapacityCommitmentRequest],
                    ~.CapacityCommitment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_capacity_commitment" not in self._stubs:
            self._stubs["get_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetCapacityCommitment",
                request_serializer=reservation.GetCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["get_capacity_commitment"]

    @property
    def delete_capacity_commitment(
        self,
    ) -> Callable[[reservation.DeleteCapacityCommitmentRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete capacity commitment method over gRPC.

        Deletes a capacity commitment. Attempting to delete capacity
        commitment before its commitment_end_time will fail with the
        error code ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.DeleteCapacityCommitmentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_capacity_commitment" not in self._stubs:
            self._stubs["delete_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteCapacityCommitment",
                request_serializer=reservation.DeleteCapacityCommitmentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_capacity_commitment"]

    @property
    def update_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.UpdateCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        r"""Return a callable for the update capacity commitment method over gRPC.

        Updates an existing capacity commitment.

        Only ``plan`` and ``renewal_plan`` fields can be updated.

        Plan can only be changed to a plan of a longer commitment
        period. Attempting to change to a plan with shorter commitment
        period will fail with the error code
        ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.UpdateCapacityCommitmentRequest],
                    ~.CapacityCommitment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_capacity_commitment" not in self._stubs:
            self._stubs["update_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateCapacityCommitment",
                request_serializer=reservation.UpdateCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["update_capacity_commitment"]

    @property
    def split_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.SplitCapacityCommitmentRequest],
        reservation.SplitCapacityCommitmentResponse,
    ]:
        r"""Return a callable for the split capacity commitment method over gRPC.

        Splits capacity commitment to two commitments of the same plan
        and ``commitment_end_time``.

        A common use case is to enable downgrading commitments.

        For example, in order to downgrade from 10000 slots to 8000, you
        might split a 10000 capacity commitment into commitments of 2000
        and 8000. Then, you would change the plan of the first one to
        ``FLEX`` and then delete it.

        Returns:
            Callable[[~.SplitCapacityCommitmentRequest],
                    ~.SplitCapacityCommitmentResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "split_capacity_commitment" not in self._stubs:
            self._stubs["split_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SplitCapacityCommitment",
                request_serializer=reservation.SplitCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.SplitCapacityCommitmentResponse.deserialize,
            )
        return self._stubs["split_capacity_commitment"]

    @property
    def merge_capacity_commitments(
        self,
    ) -> Callable[
        [reservation.MergeCapacityCommitmentsRequest], reservation.CapacityCommitment
    ]:
        r"""Return a callable for the merge capacity commitments method over gRPC.

        Merges capacity commitments of the same plan into a single
        commitment.

        The resulting capacity commitment has the greater
        commitment_end_time out of the to-be-merged capacity
        commitments.

        Attempting to merge capacity commitments of different plan will
        fail with the error code
        ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.MergeCapacityCommitmentsRequest],
                    ~.CapacityCommitment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "merge_capacity_commitments" not in self._stubs:
            self._stubs["merge_capacity_commitments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/MergeCapacityCommitments",
                request_serializer=reservation.MergeCapacityCommitmentsRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["merge_capacity_commitments"]

    @property
    def create_assignment(
        self,
    ) -> Callable[[reservation.CreateAssignmentRequest], reservation.Assignment]:
        r"""Return a callable for the create assignment method over gRPC.

        Creates an assignment object which allows the given project to
        submit jobs of a certain type using slots from the specified
        reservation.

        Currently a resource (project, folder, organization) can only
        have one assignment per each (job_type, location) combination,
        and that reservation will be used for all jobs of the matching
        type.

        Different assignments can be created on different levels of the
        projects, folders or organization hierarchy. During query
        execution, the assignment is looked up at the project, folder
        and organization levels in that order. The first assignment
        found is applied to the query.

        When creating assignments, it does not matter if other
        assignments exist at higher levels.

        Example:

        -  The organization ``organizationA`` contains two projects,
           ``project1`` and ``project2``.
        -  Assignments for all three entities (``organizationA``,
           ``project1``, and ``project2``) could all be created and
           mapped to the same or different reservations.

        "None" assignments represent an absence of the assignment.
        Projects assigned to None use on-demand pricing. To create a
        "None" assignment, use "none" as a reservation_id in the parent.
        Example parent:
        ``projects/myproject/locations/US/reservations/none``.

        Returns ``google.rpc.Code.PERMISSION_DENIED`` if user does not
        have 'bigquery.admin' permissions on the project using the
        reservation and the project that owns this reservation.

        Returns ``google.rpc.Code.INVALID_ARGUMENT`` when location of
        the assignment does not match location of the reservation.

        Returns:
            Callable[[~.CreateAssignmentRequest],
                    ~.Assignment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_assignment" not in self._stubs:
            self._stubs["create_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateAssignment",
                request_serializer=reservation.CreateAssignmentRequest.serialize,
                response_deserializer=reservation.Assignment.deserialize,
            )
        return self._stubs["create_assignment"]

    @property
    def list_assignments(
        self,
    ) -> Callable[
        [reservation.ListAssignmentsRequest], reservation.ListAssignmentsResponse
    ]:
        r"""Return a callable for the list assignments method over gRPC.

        Lists assignments.

        Only explicitly created assignments will be returned.

        Example:

        -  Organization ``organizationA`` contains two projects,
           ``project1`` and ``project2``.
        -  Reservation ``res1`` exists and was created previously.
        -  CreateAssignment was used previously to define the following
           associations between entities and reservations:
           ``<organizationA, res1>`` and ``<project1, res1>``

        In this example, ListAssignments will just return the above two
        assignments for reservation ``res1``, and no expansion/merge
        will happen.

        The wildcard "-" can be used for reservations in the request. In
        that case all assignments belongs to the specified project and
        location will be listed.

        **Note** "-" cannot be used for projects nor locations.

        Returns:
            Callable[[~.ListAssignmentsRequest],
                    ~.ListAssignmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_assignments" not in self._stubs:
            self._stubs["list_assignments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListAssignments",
                request_serializer=reservation.ListAssignmentsRequest.serialize,
                response_deserializer=reservation.ListAssignmentsResponse.deserialize,
            )
        return self._stubs["list_assignments"]

    @property
    def delete_assignment(
        self,
    ) -> Callable[[reservation.DeleteAssignmentRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete assignment method over gRPC.

        Deletes a assignment. No expansion will happen.

        Example:

        -  Organization ``organizationA`` contains two projects,
           ``project1`` and ``project2``.
        -  Reservation ``res1`` exists and was created previously.
        -  CreateAssignment was used previously to define the following
           associations between entities and reservations:
           ``<organizationA, res1>`` and ``<project1, res1>``

        In this example, deletion of the ``<organizationA, res1>``
        assignment won't affect the other assignment
        ``<project1, res1>``. After said deletion, queries from
        ``project1`` will still use ``res1`` while queries from
        ``project2`` will switch to use on-demand mode.

        Returns:
            Callable[[~.DeleteAssignmentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_assignment" not in self._stubs:
            self._stubs["delete_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteAssignment",
                request_serializer=reservation.DeleteAssignmentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_assignment"]

    @property
    def search_assignments(
        self,
    ) -> Callable[
        [reservation.SearchAssignmentsRequest], reservation.SearchAssignmentsResponse
    ]:
        r"""Return a callable for the search assignments method over gRPC.

        Deprecated: Looks up assignments for a specified resource for a
        particular region. If the request is about a project:

        1. Assignments created on the project will be returned if they
           exist.
        2. Otherwise assignments created on the closest ancestor will be
           returned.
        3. Assignments for different JobTypes will all be returned.

        The same logic applies if the request is about a folder.

        If the request is about an organization, then assignments
        created on the organization will be returned (organization
        doesn't have ancestors).

        Comparing to ListAssignments, there are some behavior
        differences:

        1. permission on the assignee will be verified in this API.
        2. Hierarchy lookup (project->folder->organization) happens in
           this API.
        3. Parent here is ``projects/*/locations/*``, instead of
           ``projects/*/locations/*reservations/*``.

        **Note** "-" cannot be used for projects nor locations.

        Returns:
            Callable[[~.SearchAssignmentsRequest],
                    ~.SearchAssignmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_assignments" not in self._stubs:
            self._stubs["search_assignments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SearchAssignments",
                request_serializer=reservation.SearchAssignmentsRequest.serialize,
                response_deserializer=reservation.SearchAssignmentsResponse.deserialize,
            )
        return self._stubs["search_assignments"]

    @property
    def search_all_assignments(
        self,
    ) -> Callable[
        [reservation.SearchAllAssignmentsRequest],
        reservation.SearchAllAssignmentsResponse,
    ]:
        r"""Return a callable for the search all assignments method over gRPC.

        Looks up assignments for a specified resource for a particular
        region. If the request is about a project:

        1. Assignments created on the project will be returned if they
           exist.
        2. Otherwise assignments created on the closest ancestor will be
           returned.
        3. Assignments for different JobTypes will all be returned.

        The same logic applies if the request is about a folder.

        If the request is about an organization, then assignments
        created on the organization will be returned (organization
        doesn't have ancestors).

        Comparing to ListAssignments, there are some behavior
        differences:

        1. permission on the assignee will be verified in this API.
        2. Hierarchy lookup (project->folder->organization) happens in
           this API.
        3. Parent here is ``projects/*/locations/*``, instead of
           ``projects/*/locations/*reservations/*``.

        Returns:
            Callable[[~.SearchAllAssignmentsRequest],
                    ~.SearchAllAssignmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_all_assignments" not in self._stubs:
            self._stubs["search_all_assignments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SearchAllAssignments",
                request_serializer=reservation.SearchAllAssignmentsRequest.serialize,
                response_deserializer=reservation.SearchAllAssignmentsResponse.deserialize,
            )
        return self._stubs["search_all_assignments"]

    @property
    def move_assignment(
        self,
    ) -> Callable[[reservation.MoveAssignmentRequest], reservation.Assignment]:
        r"""Return a callable for the move assignment method over gRPC.

        Moves an assignment under a new reservation.
        This differs from removing an existing assignment and
        recreating a new one by providing a transactional change
        that ensures an assignee always has an associated
        reservation.

        Returns:
            Callable[[~.MoveAssignmentRequest],
                    ~.Assignment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_assignment" not in self._stubs:
            self._stubs["move_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/MoveAssignment",
                request_serializer=reservation.MoveAssignmentRequest.serialize,
                response_deserializer=reservation.Assignment.deserialize,
            )
        return self._stubs["move_assignment"]

    @property
    def get_bi_reservation(
        self,
    ) -> Callable[[reservation.GetBiReservationRequest], reservation.BiReservation]:
        r"""Return a callable for the get bi reservation method over gRPC.

        Retrieves a BI reservation.

        Returns:
            Callable[[~.GetBiReservationRequest],
                    ~.BiReservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_bi_reservation" not in self._stubs:
            self._stubs["get_bi_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetBiReservation",
                request_serializer=reservation.GetBiReservationRequest.serialize,
                response_deserializer=reservation.BiReservation.deserialize,
            )
        return self._stubs["get_bi_reservation"]

    @property
    def update_bi_reservation(
        self,
    ) -> Callable[[reservation.UpdateBiReservationRequest], reservation.BiReservation]:
        r"""Return a callable for the update bi reservation method over gRPC.

        Updates a BI reservation.

        Only fields specified in the ``field_mask`` are updated.

        A singleton BI reservation always exists with default size 0. In
        order to reserve BI capacity it needs to be updated to an amount
        greater than 0. In order to release BI capacity reservation size
        must be set to 0.

        Returns:
            Callable[[~.UpdateBiReservationRequest],
                    ~.BiReservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_bi_reservation" not in self._stubs:
            self._stubs["update_bi_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateBiReservation",
                request_serializer=reservation.UpdateBiReservationRequest.serialize,
                response_deserializer=reservation.BiReservation.deserialize,
            )
        return self._stubs["update_bi_reservation"]


__all__ = ("ReservationServiceGrpcTransport",)

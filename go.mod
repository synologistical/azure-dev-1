module github.com/azure/azure-dev

go 1.24

require (
	dario.cat/mergo v1.0.1
	github.com/AlecAivazis/survey/v2 v2.3.7
	github.com/Azure/azure-sdk-for-go/sdk/azcore v1.17.0
	github.com/Azure/azure-sdk-for-go/sdk/azidentity v1.8.2
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/apimanagement/armapimanagement v1.1.1
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/appconfiguration/armappconfiguration v1.0.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/appcontainers/armappcontainers/v3 v3.0.0-beta.1
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/appplatform/armappplatform/v2 v2.0.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/appservice/armappservice/v2 v2.3.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/authorization/armauthorization/v2 v2.2.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/cognitiveservices/armcognitiveservices v1.6.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/containerregistry/armcontainerregistry v1.2.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/containerservice/armcontainerservice/v2 v2.4.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/cosmos/armcosmos/v2 v2.6.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/keyvault/armkeyvault v1.4.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/machinelearning/armmachinelearning/v3 v3.2.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/msi/armmsi v1.2.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resourcegraph/armresourcegraph v0.7.1
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armdeploymentstacks v1.0.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armresources v1.2.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armsubscriptions v1.3.0
	github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/sql/armsql/v2 v2.0.0-beta.4
	github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets v1.3.1
	github.com/Azure/azure-sdk-for-go/sdk/storage/azblob v1.3.1
	github.com/Azure/azure-sdk-for-go/sdk/storage/azfile v1.2.2
	github.com/Azure/azure-storage-file-go v0.8.0
	github.com/AzureAD/microsoft-authentication-library-for-go v1.4.2
	github.com/MakeNowJust/heredoc/v2 v2.0.1
	github.com/Masterminds/semver/v3 v3.3.1
	github.com/adam-lavrik/go-imath v0.0.0-20210910152346-265a42a96f0b
	github.com/benbjohnson/clock v1.3.5
	github.com/blang/semver/v4 v4.0.0
	github.com/bmatcuk/doublestar/v4 v4.8.1
	github.com/bradleyjkemp/cupaloy/v2 v2.8.0
	github.com/braydonk/yaml v0.9.0
	github.com/buger/goterm v1.0.4
	github.com/cli/browser v1.3.0
	github.com/denormal/go-gitignore v0.0.0-20180930084346-ae8ad1d07817
	github.com/drone/envsubst v1.0.3
	github.com/eiannone/keyboard v0.0.0-20220611211555-0d226195f203
	github.com/fatih/color v1.18.0
	github.com/fsnotify/fsnotify v1.9.0
	github.com/gofrs/flock v0.12.1
	github.com/golang-jwt/jwt/v5 v5.2.2
	github.com/golobby/container/v3 v3.3.2
	github.com/google/uuid v1.6.0
	github.com/gorilla/websocket v1.5.3
	github.com/joho/godotenv v1.5.1
	github.com/magefile/mage v1.15.0
	github.com/mattn/go-colorable v0.1.14
	github.com/mattn/go-isatty v0.0.20
	github.com/microsoft/ApplicationInsights-Go v0.4.4
	github.com/microsoft/azure-devops-go-api/azuredevops/v7 v7.1.0
	github.com/microsoft/go-deviceid v1.0.0
	github.com/moby/patternmatcher v0.6.0
	github.com/nathan-fiscaletti/consolesize-go v0.0.0-20220204101620-317176b6684d
	github.com/otiai10/copy v1.14.1
	github.com/psanford/memfs v0.0.0-20241019191636-4ef911798f9b
	github.com/sergi/go-diff v1.3.1
	github.com/sethvargo/go-retry v0.3.0
	github.com/spf13/cobra v1.9.1
	github.com/spf13/pflag v1.0.6
	github.com/stretchr/testify v1.10.0
	github.com/theckman/yacspin v0.13.12
	github.com/tidwall/gjson v1.18.0
	github.com/tmc/langchaingo v0.1.13
	go.lsp.dev/jsonrpc2 v0.10.0
	go.opentelemetry.io/otel v1.35.0
	go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp v1.35.0
	go.opentelemetry.io/otel/exporters/stdout/stdouttrace v1.35.0
	go.opentelemetry.io/otel/sdk v1.35.0
	go.opentelemetry.io/otel/trace v1.35.0
	go.uber.org/atomic v1.11.0
	go.uber.org/multierr v1.11.0
	golang.org/x/sys v0.32.0
	google.golang.org/grpc v1.71.1
	google.golang.org/protobuf v1.36.6
	gopkg.in/dnaeon/go-vcr.v3 v3.2.0
	gopkg.in/yaml.v3 v3.0.1
)

require (
	github.com/Azure/azure-pipeline-go v0.2.1 // indirect
	github.com/Azure/azure-sdk-for-go/sdk/internal v1.10.0 // indirect
	github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/internal v1.1.1 // indirect
	github.com/cenkalti/backoff/v4 v4.3.0 // indirect
	github.com/danwakefield/fnmatch v0.0.0-20160403171240-cbb64ac3d964 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/dlclark/regexp2 v1.10.0 // indirect
	github.com/go-logr/logr v1.4.2 // indirect
	github.com/go-logr/stdr v1.2.2 // indirect
	github.com/grpc-ecosystem/grpc-gateway/v2 v2.26.3 // indirect
	github.com/inconshreveable/mousetrap v1.1.0 // indirect
	github.com/kballard/go-shellquote v0.0.0-20180428030007-95032a82bc51 // indirect
	github.com/kylelemons/godebug v1.1.0 // indirect
	github.com/mattn/go-ieproxy v0.0.12 // indirect
	github.com/mattn/go-runewidth v0.0.16 // indirect
	github.com/mgutz/ansi v0.0.0-20200706080929-d51e80ef957d // indirect
	github.com/otiai10/mint v1.6.3 // indirect
	github.com/pkg/browser v0.0.0-20240102092130-5ac0b6a4141c // indirect
	github.com/pkoukk/tiktoken-go v0.1.6 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/rivo/uniseg v0.4.7 // indirect
	github.com/segmentio/asm v1.2.0 // indirect
	github.com/segmentio/encoding v0.4.1 // indirect
	github.com/stretchr/objx v0.5.2 // indirect
	github.com/tidwall/match v1.1.1 // indirect
	github.com/tidwall/pretty v1.2.1 // indirect
	go.opentelemetry.io/auto/sdk v1.1.0 // indirect
	go.opentelemetry.io/otel/exporters/otlp/otlptrace v1.35.0 // indirect
	go.opentelemetry.io/otel/metric v1.35.0 // indirect
	go.opentelemetry.io/proto/otlp v1.5.0 // indirect
	golang.org/x/crypto v0.37.0 // indirect
	golang.org/x/net v0.39.0 // indirect
	golang.org/x/sync v0.13.0 // indirect
	golang.org/x/term v0.31.0 // indirect
	golang.org/x/text v0.24.0 // indirect
	google.golang.org/genproto/googleapis/api v0.0.0-20250407143221-ac9807e6c755 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20250407143221-ac9807e6c755 // indirect
)

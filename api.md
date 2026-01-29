# Shared Types

```python
from jocall3.types import Address, Transaction
```

# Users

Types:

```python
from jocall3.types import UserLoginResponse, UserRegisterResponse
```

Methods:

- <code title="post /users/login">client.users.<a href="./src/jocall3/resources/users/users.py">login</a>(\*\*<a href="src/jocall3/types/user_login_params.py">params</a>) -> <a href="./src/jocall3/types/user_login_response.py">UserLoginResponse</a></code>
- <code title="post /users/logout">client.users.<a href="./src/jocall3/resources/users/users.py">logout</a>() -> None</code>
- <code title="post /users/register">client.users.<a href="./src/jocall3/resources/users/users.py">register</a>(\*\*<a href="src/jocall3/types/user_register_params.py">params</a>) -> <a href="./src/jocall3/types/user_register_response.py">UserRegisterResponse</a></code>

## PasswordReset

Types:

```python
from jocall3.types.users import PasswordResetConfirmResponse, PasswordResetInitiateResponse
```

Methods:

- <code title="post /users/password-reset/confirm">client.users.password_reset.<a href="./src/jocall3/resources/users/password_reset.py">confirm</a>(\*\*<a href="src/jocall3/types/users/password_reset_confirm_params.py">params</a>) -> <a href="./src/jocall3/types/users/password_reset_confirm_response.py">PasswordResetConfirmResponse</a></code>
- <code title="post /users/password-reset/initiate">client.users.password_reset.<a href="./src/jocall3/resources/users/password_reset.py">initiate</a>(\*\*<a href="src/jocall3/types/users/password_reset_initiate_params.py">params</a>) -> <a href="./src/jocall3/types/users/password_reset_initiate_response.py">PasswordResetInitiateResponse</a></code>

## Me

Types:

```python
from jocall3.types.users import MeRetrieveResponse
```

Methods:

- <code title="get /users/me">client.users.me.<a href="./src/jocall3/resources/users/me/me.py">retrieve</a>() -> <a href="./src/jocall3/types/users/me_retrieve_response.py">MeRetrieveResponse</a></code>
- <code title="put /users/me">client.users.me.<a href="./src/jocall3/resources/users/me/me.py">update</a>() -> None</code>
- <code title="delete /users/me">client.users.me.<a href="./src/jocall3/resources/users/me/me.py">delete</a>() -> None</code>

### Preferences

Types:

```python
from jocall3.types.users.me import PreferenceRetrieveResponse, PreferenceUpdateResponse
```

Methods:

- <code title="get /users/me/preferences">client.users.me.preferences.<a href="./src/jocall3/resources/users/me/preferences.py">retrieve</a>() -> <a href="./src/jocall3/types/users/me/preference_retrieve_response.py">PreferenceRetrieveResponse</a></code>
- <code title="put /users/me/preferences">client.users.me.preferences.<a href="./src/jocall3/resources/users/me/preferences.py">update</a>(\*\*<a href="src/jocall3/types/users/me/preference_update_params.py">params</a>) -> <a href="./src/jocall3/types/users/me/preference_update_response.py">PreferenceUpdateResponse</a></code>

### Security

Types:

```python
from jocall3.types.users.me import SecurityRetrieveLogResponse, SecurityRotateKeysResponse
```

Methods:

- <code title="get /users/me/security/log">client.users.me.security.<a href="./src/jocall3/resources/users/me/security.py">retrieve_log</a>(\*\*<a href="src/jocall3/types/users/me/security_retrieve_log_params.py">params</a>) -> <a href="./src/jocall3/types/users/me/security_retrieve_log_response.py">SecurityRetrieveLogResponse</a></code>
- <code title="post /users/me/security/rotate-keys">client.users.me.security.<a href="./src/jocall3/resources/users/me/security.py">rotate_keys</a>() -> <a href="./src/jocall3/types/users/me/security_rotate_keys_response.py">SecurityRotateKeysResponse</a></code>

### Devices

Types:

```python
from jocall3.types.users.me import DeviceListResponse
```

Methods:

- <code title="get /users/me/devices">client.users.me.devices.<a href="./src/jocall3/resources/users/me/devices.py">list</a>() -> <a href="./src/jocall3/types/users/me/device_list_response.py">DeviceListResponse</a></code>
- <code title="delete /users/me/devices/{deviceId}">client.users.me.devices.<a href="./src/jocall3/resources/users/me/devices.py">deregister</a>(device_id) -> None</code>
- <code title="post /users/me/devices">client.users.me.devices.<a href="./src/jocall3/resources/users/me/devices.py">register</a>(\*\*<a href="src/jocall3/types/users/me/device_register_params.py">params</a>) -> None</code>

### Biometrics

Types:

```python
from jocall3.types.users.me import BiometricRetrieveStatusResponse, BiometricVerifyResponse
```

Methods:

- <code title="delete /users/me/biometrics">client.users.me.biometrics.<a href="./src/jocall3/resources/users/me/biometrics.py">delete</a>() -> None</code>
- <code title="post /users/me/biometrics/enroll">client.users.me.biometrics.<a href="./src/jocall3/resources/users/me/biometrics.py">enroll</a>(\*\*<a href="src/jocall3/types/users/me/biometric_enroll_params.py">params</a>) -> None</code>
- <code title="get /users/me/biometrics">client.users.me.biometrics.<a href="./src/jocall3/resources/users/me/biometrics.py">retrieve_status</a>() -> <a href="./src/jocall3/types/users/me/biometric_retrieve_status_response.py">BiometricRetrieveStatusResponse</a></code>
- <code title="post /users/me/biometrics/verify">client.users.me.biometrics.<a href="./src/jocall3/resources/users/me/biometrics.py">verify</a>(\*\*<a href="src/jocall3/types/users/me/biometric_verify_params.py">params</a>) -> <a href="./src/jocall3/types/users/me/biometric_verify_response.py">BiometricVerifyResponse</a></code>

# Accounts

Types:

```python
from jocall3.types import (
    AccountListResponse,
    AccountLinkResponse,
    AccountOpenResponse,
    AccountRetrieveDetailsResponse,
)
```

Methods:

- <code title="get /accounts/me">client.accounts.<a href="./src/jocall3/resources/accounts/accounts.py">list</a>() -> <a href="./src/jocall3/types/account_list_response.py">AccountListResponse</a></code>
- <code title="delete /accounts/{accountId}">client.accounts.<a href="./src/jocall3/resources/accounts/accounts.py">close</a>(account_id) -> None</code>
- <code title="post /accounts/link">client.accounts.<a href="./src/jocall3/resources/accounts/accounts.py">link</a>(\*\*<a href="src/jocall3/types/account_link_params.py">params</a>) -> <a href="./src/jocall3/types/account_link_response.py">AccountLinkResponse</a></code>
- <code title="post /accounts/open">client.accounts.<a href="./src/jocall3/resources/accounts/accounts.py">open</a>(\*\*<a href="src/jocall3/types/account_open_params.py">params</a>) -> <a href="./src/jocall3/types/account_open_response.py">AccountOpenResponse</a></code>
- <code title="get /accounts/{accountId}/details">client.accounts.<a href="./src/jocall3/resources/accounts/accounts.py">retrieve_details</a>(account_id) -> <a href="./src/jocall3/types/account_retrieve_details_response.py">AccountRetrieveDetailsResponse</a></code>

## Transactions

Types:

```python
from jocall3.types.accounts import TransactionListArchivedResponse, TransactionListPendingResponse
```

Methods:

- <code title="get /accounts/{accountId}/transactions/archived">client.accounts.transactions.<a href="./src/jocall3/resources/accounts/transactions.py">list_archived</a>(account_id, \*\*<a href="src/jocall3/types/accounts/transaction_list_archived_params.py">params</a>) -> <a href="./src/jocall3/types/accounts/transaction_list_archived_response.py">TransactionListArchivedResponse</a></code>
- <code title="get /accounts/{accountId}/transactions/pending">client.accounts.transactions.<a href="./src/jocall3/resources/accounts/transactions.py">list_pending</a>(account_id) -> <a href="./src/jocall3/types/accounts/transaction_list_pending_response.py">TransactionListPendingResponse</a></code>

## BalanceHistory

Types:

```python
from jocall3.types.accounts import BalanceHistoryRetrieveResponse
```

Methods:

- <code title="get /accounts/{accountId}/balance-history">client.accounts.balance_history.<a href="./src/jocall3/resources/accounts/balance_history.py">retrieve</a>(account_id, \*\*<a href="src/jocall3/types/accounts/balance_history_retrieve_params.py">params</a>) -> <a href="./src/jocall3/types/accounts/balance_history_retrieve_response.py">BalanceHistoryRetrieveResponse</a></code>

## Statements

Types:

```python
from jocall3.types.accounts import StatementListResponse
```

Methods:

- <code title="get /accounts/{accountId}/statements">client.accounts.statements.<a href="./src/jocall3/resources/accounts/statements.py">list</a>(account_id) -> <a href="./src/jocall3/types/accounts/statement_list_response.py">StatementListResponse</a></code>
- <code title="get /accounts/{accountId}/statements/{statementId}/pdf">client.accounts.statements.<a href="./src/jocall3/resources/accounts/statements.py">download_pdf</a>(statement_id, \*, account_id) -> BinaryAPIResponse</code>

## Overdraft

Types:

```python
from jocall3.types.accounts import OverdraftRetrieveSettingsResponse
```

Methods:

- <code title="get /accounts/{accountId}/overdraft-settings">client.accounts.overdraft.<a href="./src/jocall3/resources/accounts/overdraft.py">retrieve_settings</a>(account_id) -> <a href="./src/jocall3/types/accounts/overdraft_retrieve_settings_response.py">OverdraftRetrieveSettingsResponse</a></code>
- <code title="put /accounts/{accountId}/overdraft-settings">client.accounts.overdraft.<a href="./src/jocall3/resources/accounts/overdraft.py">update_settings</a>(account_id, \*\*<a href="src/jocall3/types/accounts/overdraft_update_settings_params.py">params</a>) -> None</code>

# Transactions

Types:

```python
from jocall3.types import TransactionListResponse
```

Methods:

- <code title="get /transactions/{transactionId}">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">retrieve</a>(transaction_id) -> <a href="./src/jocall3/types/shared/transaction.py">Transaction</a></code>
- <code title="get /transactions">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">list</a>(\*\*<a href="src/jocall3/types/transaction_list_params.py">params</a>) -> <a href="./src/jocall3/types/transaction_list_response.py">TransactionListResponse</a></code>
- <code title="put /transactions/{transactionId}/notes">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">add_notes</a>(transaction_id, \*\*<a href="src/jocall3/types/transaction_add_notes_params.py">params</a>) -> None</code>
- <code title="put /transactions/{transactionId}/categorize">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">categorize</a>(transaction_id, \*\*<a href="src/jocall3/types/transaction_categorize_params.py">params</a>) -> <a href="./src/jocall3/types/shared/transaction.py">Transaction</a></code>
- <code title="post /transactions/{transactionId}/dispute">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">dispute</a>(transaction_id, \*\*<a href="src/jocall3/types/transaction_dispute_params.py">params</a>) -> None</code>
- <code title="post /transactions/{transactionId}/split">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">split</a>(transaction_id, \*\*<a href="src/jocall3/types/transaction_split_params.py">params</a>) -> None</code>

## Recurring

Types:

```python
from jocall3.types.transactions import RecurringListResponse
```

Methods:

- <code title="post /transactions/recurring">client.transactions.recurring.<a href="./src/jocall3/resources/transactions/recurring.py">create</a>(\*\*<a href="src/jocall3/types/transactions/recurring_create_params.py">params</a>) -> None</code>
- <code title="get /transactions/recurring">client.transactions.recurring.<a href="./src/jocall3/resources/transactions/recurring.py">list</a>() -> <a href="./src/jocall3/types/transactions/recurring_list_response.py">RecurringListResponse</a></code>
- <code title="delete /transactions/recurring/{recurringId}">client.transactions.recurring.<a href="./src/jocall3/resources/transactions/recurring.py">cancel</a>(recurring_id) -> None</code>

## Insights

Types:

```python
from jocall3.types.transactions import (
    InsightRetrieveFutureFlowResponse,
    InsightRetrieveSpendingTrendsResponse,
)
```

Methods:

- <code title="get /transactions/insights/future-flow">client.transactions.insights.<a href="./src/jocall3/resources/transactions/insights.py">retrieve_future_flow</a>() -> <a href="./src/jocall3/types/transactions/insight_retrieve_future_flow_response.py">InsightRetrieveFutureFlowResponse</a></code>
- <code title="get /transactions/insights/spending-trends">client.transactions.insights.<a href="./src/jocall3/resources/transactions/insights.py">retrieve_spending_trends</a>() -> <a href="./src/jocall3/types/transactions/insight_retrieve_spending_trends_response.py">InsightRetrieveSpendingTrendsResponse</a></code>

# AI

## Advisor

Types:

```python
from jocall3.types.ai import AdvisorChatResponse, AdvisorRetrieveHistoryResponse
```

Methods:

- <code title="post /ai/advisor/chat">client.ai.advisor.<a href="./src/jocall3/resources/ai/advisor/advisor.py">chat</a>(\*\*<a href="src/jocall3/types/ai/advisor_chat_params.py">params</a>) -> <a href="./src/jocall3/types/ai/advisor_chat_response.py">AdvisorChatResponse</a></code>
- <code title="get /ai/advisor/chat/history">client.ai.advisor.<a href="./src/jocall3/resources/ai/advisor/advisor.py">retrieve_history</a>() -> <a href="./src/jocall3/types/ai/advisor_retrieve_history_response.py">AdvisorRetrieveHistoryResponse</a></code>

### Tools

Types:

```python
from jocall3.types.ai.advisor import ToolListResponse
```

Methods:

- <code title="get /ai/advisor/tools">client.ai.advisor.tools.<a href="./src/jocall3/resources/ai/advisor/tools.py">list</a>() -> <a href="./src/jocall3/types/ai/advisor/tool_list_response.py">ToolListResponse</a></code>
- <code title="post /ai/advisor/tools/{toolId}/enable">client.ai.advisor.tools.<a href="./src/jocall3/resources/ai/advisor/tools.py">enable</a>(tool_id) -> None</code>

## Oracle

### Simulate

Types:

```python
from jocall3.types.ai.oracle import SimulateRunAdvancedResponse, SimulateRunStandardResponse
```

Methods:

- <code title="post /ai/oracle/simulate/advanced">client.ai.oracle.simulate.<a href="./src/jocall3/resources/ai/oracle/simulate.py">run_advanced</a>(\*\*<a href="src/jocall3/types/ai/oracle/simulate_run_advanced_params.py">params</a>) -> <a href="./src/jocall3/types/ai/oracle/simulate_run_advanced_response.py">SimulateRunAdvancedResponse</a></code>
- <code title="post /ai/oracle/simulate/monte-carlo">client.ai.oracle.simulate.<a href="./src/jocall3/resources/ai/oracle/simulate.py">run_monte_carlo</a>(\*\*<a href="src/jocall3/types/ai/oracle/simulate_run_monte_carlo_params.py">params</a>) -> None</code>
- <code title="post /ai/oracle/simulate">client.ai.oracle.simulate.<a href="./src/jocall3/resources/ai/oracle/simulate.py">run_standard</a>(\*\*<a href="src/jocall3/types/ai/oracle/simulate_run_standard_params.py">params</a>) -> <a href="./src/jocall3/types/ai/oracle/simulate_run_standard_response.py">SimulateRunStandardResponse</a></code>

### Predictions

Types:

```python
from jocall3.types.ai.oracle import (
    PredictionRetrieveInflationForecastResponse,
    PredictionRetrieveMarketCrashProbabilityResponse,
)
```

Methods:

- <code title="get /ai/oracle/predictions/inflation">client.ai.oracle.predictions.<a href="./src/jocall3/resources/ai/oracle/predictions.py">retrieve_inflation_forecast</a>(\*\*<a href="src/jocall3/types/ai/oracle/prediction_retrieve_inflation_forecast_params.py">params</a>) -> <a href="./src/jocall3/types/ai/oracle/prediction_retrieve_inflation_forecast_response.py">PredictionRetrieveInflationForecastResponse</a></code>
- <code title="get /ai/oracle/predictions/market-crash-probability">client.ai.oracle.predictions.<a href="./src/jocall3/resources/ai/oracle/predictions.py">retrieve_market_crash_probability</a>() -> <a href="./src/jocall3/types/ai/oracle/prediction_retrieve_market_crash_probability_response.py">PredictionRetrieveMarketCrashProbabilityResponse</a></code>

### Simulations

Types:

```python
from jocall3.types.ai.oracle import SimulationRetrieveResponse, SimulationListResponse
```

Methods:

- <code title="get /ai/oracle/simulations/{simulationId}">client.ai.oracle.simulations.<a href="./src/jocall3/resources/ai/oracle/simulations.py">retrieve</a>(simulation_id) -> <a href="./src/jocall3/types/ai/oracle/simulation_retrieve_response.py">SimulationRetrieveResponse</a></code>
- <code title="get /ai/oracle/simulations">client.ai.oracle.simulations.<a href="./src/jocall3/resources/ai/oracle/simulations.py">list</a>() -> <a href="./src/jocall3/types/ai/oracle/simulation_list_response.py">SimulationListResponse</a></code>

## Incubator

Types:

```python
from jocall3.types.ai import (
    IncubatorListPitchesResponse,
    IncubatorSubmitPitchResponse,
    IncubatorValidateIdeaResponse,
)
```

Methods:

- <code title="get /ai/incubator/pitches">client.ai.incubator.<a href="./src/jocall3/resources/ai/incubator/incubator.py">list_pitches</a>() -> <a href="./src/jocall3/types/ai/incubator_list_pitches_response.py">IncubatorListPitchesResponse</a></code>
- <code title="post /ai/incubator/pitch">client.ai.incubator.<a href="./src/jocall3/resources/ai/incubator/incubator.py">submit_pitch</a>(\*\*<a href="src/jocall3/types/ai/incubator_submit_pitch_params.py">params</a>) -> <a href="./src/jocall3/types/ai/incubator_submit_pitch_response.py">IncubatorSubmitPitchResponse</a></code>
- <code title="post /ai/incubator/validate">client.ai.incubator.<a href="./src/jocall3/resources/ai/incubator/incubator.py">validate_idea</a>(\*\*<a href="src/jocall3/types/ai/incubator_validate_idea_params.py">params</a>) -> <a href="./src/jocall3/types/ai/incubator_validate_idea_response.py">IncubatorValidateIdeaResponse</a></code>

### Analysis

Types:

```python
from jocall3.types.ai.incubator import AnalysisGenerateSwotResponse, AnalysisScanCompetitorsResponse
```

Methods:

- <code title="post /ai/incubator/analysis/swot">client.ai.incubator.analysis.<a href="./src/jocall3/resources/ai/incubator/analysis.py">generate_swot</a>(\*\*<a href="src/jocall3/types/ai/incubator/analysis_generate_swot_params.py">params</a>) -> <a href="./src/jocall3/types/ai/incubator/analysis_generate_swot_response.py">AnalysisGenerateSwotResponse</a></code>
- <code title="post /ai/incubator/analysis/competitors">client.ai.incubator.analysis.<a href="./src/jocall3/resources/ai/incubator/analysis.py">scan_competitors</a>(\*\*<a href="src/jocall3/types/ai/incubator/analysis_scan_competitors_params.py">params</a>) -> <a href="./src/jocall3/types/ai/incubator/analysis_scan_competitors_response.py">AnalysisScanCompetitorsResponse</a></code>

### Pitch

Types:

```python
from jocall3.types.ai.incubator import PitchRetrieveDetailsResponse
```

Methods:

- <code title="get /ai/incubator/pitch/{pitchId}/details">client.ai.incubator.pitch.<a href="./src/jocall3/resources/ai/incubator/pitch.py">retrieve_details</a>(pitch_id) -> <a href="./src/jocall3/types/ai/incubator/pitch_retrieve_details_response.py">PitchRetrieveDetailsResponse</a></code>
- <code title="put /ai/incubator/pitch/{pitchId}/feedback">client.ai.incubator.pitch.<a href="./src/jocall3/resources/ai/incubator/pitch.py">submit_feedback</a>(pitch_id, \*\*<a href="src/jocall3/types/ai/incubator/pitch_submit_feedback_params.py">params</a>) -> None</code>

## Ads

Types:

```python
from jocall3.types.ai import (
    AdListResponse,
    AdGenerateCopyResponse,
    AdGenerateVideoResponse,
    AdOptimizeCampaignResponse,
    AdRetrieveOperationStatusResponse,
)
```

Methods:

- <code title="get /ai/ads">client.ai.ads.<a href="./src/jocall3/resources/ai/ads.py">list</a>() -> <a href="./src/jocall3/types/ai/ad_list_response.py">AdListResponse</a></code>
- <code title="post /ai/ads/generate/copy">client.ai.ads.<a href="./src/jocall3/resources/ai/ads.py">generate_copy</a>(\*\*<a href="src/jocall3/types/ai/ad_generate_copy_params.py">params</a>) -> <a href="./src/jocall3/types/ai/ad_generate_copy_response.py">AdGenerateCopyResponse</a></code>
- <code title="post /ai/ads/generate/video">client.ai.ads.<a href="./src/jocall3/resources/ai/ads.py">generate_video</a>(\*\*<a href="src/jocall3/types/ai/ad_generate_video_params.py">params</a>) -> <a href="./src/jocall3/types/ai/ad_generate_video_response.py">AdGenerateVideoResponse</a></code>
- <code title="post /ai/ads/optimize">client.ai.ads.<a href="./src/jocall3/resources/ai/ads.py">optimize_campaign</a>(\*\*<a href="src/jocall3/types/ai/ad_optimize_campaign_params.py">params</a>) -> <a href="./src/jocall3/types/ai/ad_optimize_campaign_response.py">AdOptimizeCampaignResponse</a></code>
- <code title="get /ai/ads/operations/{operationId}">client.ai.ads.<a href="./src/jocall3/resources/ai/ads.py">retrieve_operation_status</a>(operation_id) -> <a href="./src/jocall3/types/ai/ad_retrieve_operation_status_response.py">AdRetrieveOperationStatusResponse</a></code>

## Agent

Types:

```python
from jocall3.types.ai import AgentRetrieveCapabilitiesResponse, AgentRetrievePromptsResponse
```

Methods:

- <code title="get /ai/agent/capabilities">client.ai.agent.<a href="./src/jocall3/resources/ai/agent.py">retrieve_capabilities</a>() -> <a href="./src/jocall3/types/ai/agent_retrieve_capabilities_response.py">AgentRetrieveCapabilitiesResponse</a></code>
- <code title="get /ai/agent/prompts">client.ai.agent.<a href="./src/jocall3/resources/ai/agent.py">retrieve_prompts</a>() -> <a href="./src/jocall3/types/ai/agent_retrieve_prompts_response.py">AgentRetrievePromptsResponse</a></code>
- <code title="put /ai/agent/prompts">client.ai.agent.<a href="./src/jocall3/resources/ai/agent.py">update_prompts</a>(\*\*<a href="src/jocall3/types/ai/agent_update_prompts_params.py">params</a>) -> None</code>

## Models

Types:

```python
from jocall3.types.ai import ModelFineTuneResponse, ModelListVersionsResponse
```

Methods:

- <code title="post /ai/models/fine-tune">client.ai.models.<a href="./src/jocall3/resources/ai/models.py">fine_tune</a>(\*\*<a href="src/jocall3/types/ai/model_fine_tune_params.py">params</a>) -> <a href="./src/jocall3/types/ai/model_fine_tune_response.py">ModelFineTuneResponse</a></code>
- <code title="get /ai/models/versions">client.ai.models.<a href="./src/jocall3/resources/ai/models.py">list_versions</a>() -> <a href="./src/jocall3/types/ai/model_list_versions_response.py">ModelListVersionsResponse</a></code>

# Corporate

Types:

```python
from jocall3.types import CorporateOnboardEntityResponse
```

Methods:

- <code title="post /corporate/onboard">client.corporate.<a href="./src/jocall3/resources/corporate/corporate.py">onboard_entity</a>(\*\*<a href="src/jocall3/types/corporate_onboard_entity_params.py">params</a>) -> <a href="./src/jocall3/types/corporate_onboard_entity_response.py">CorporateOnboardEntityResponse</a></code>

## Compliance

Types:

```python
from jocall3.types.corporate import (
    ComplianceScreenAdverseMediaResponse,
    ComplianceScreenPepResponse,
    ComplianceScreenSanctionsResponse,
)
```

Methods:

- <code title="post /corporate/compliance/media">client.corporate.compliance.<a href="./src/jocall3/resources/corporate/compliance/compliance.py">screen_adverse_media</a>(\*\*<a href="src/jocall3/types/corporate/compliance_screen_adverse_media_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/compliance_screen_adverse_media_response.py">ComplianceScreenAdverseMediaResponse</a></code>
- <code title="post /corporate/compliance/pep">client.corporate.compliance.<a href="./src/jocall3/resources/corporate/compliance/compliance.py">screen_pep</a>(\*\*<a href="src/jocall3/types/corporate/compliance_screen_pep_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/compliance_screen_pep_response.py">ComplianceScreenPepResponse</a></code>
- <code title="post /corporate/compliance/sanctions">client.corporate.compliance.<a href="./src/jocall3/resources/corporate/compliance/compliance.py">screen_sanctions</a>(\*\*<a href="src/jocall3/types/corporate/compliance_screen_sanctions_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/compliance_screen_sanctions_response.py">ComplianceScreenSanctionsResponse</a></code>

### Audits

Types:

```python
from jocall3.types.corporate.compliance import AuditRequestResponse, AuditRetrieveReportResponse
```

Methods:

- <code title="post /corporate/compliance/audits">client.corporate.compliance.audits.<a href="./src/jocall3/resources/corporate/compliance/audits.py">request</a>(\*\*<a href="src/jocall3/types/corporate/compliance/audit_request_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/compliance/audit_request_response.py">AuditRequestResponse</a></code>
- <code title="get /corporate/compliance/audits/{auditId}/report">client.corporate.compliance.audits.<a href="./src/jocall3/resources/corporate/compliance/audits.py">retrieve_report</a>(audit_id) -> <a href="./src/jocall3/types/corporate/compliance/audit_retrieve_report_response.py">AuditRetrieveReportResponse</a></code>

## Treasury

Types:

```python
from jocall3.types.corporate import (
    TreasuryOptimizeLiquidityResponse,
    TreasuryRetrieveCashFlowForecastResponse,
    TreasuryRetrieveLiquidityPositionsResponse,
)
```

Methods:

- <code title="post /corporate/treasury/bulk-payouts">client.corporate.treasury.<a href="./src/jocall3/resources/corporate/treasury/treasury.py">execute_bulk_payouts</a>(\*\*<a href="src/jocall3/types/corporate/treasury_execute_bulk_payouts_params.py">params</a>) -> None</code>
- <code title="post /corporate/treasury/liquidity/optimize">client.corporate.treasury.<a href="./src/jocall3/resources/corporate/treasury/treasury.py">optimize_liquidity</a>(\*\*<a href="src/jocall3/types/corporate/treasury_optimize_liquidity_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/treasury_optimize_liquidity_response.py">TreasuryOptimizeLiquidityResponse</a></code>
- <code title="get /corporate/treasury/cash-flow/forecast">client.corporate.treasury.<a href="./src/jocall3/resources/corporate/treasury/treasury.py">retrieve_cash_flow_forecast</a>(\*\*<a href="src/jocall3/types/corporate/treasury_retrieve_cash_flow_forecast_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/treasury_retrieve_cash_flow_forecast_response.py">TreasuryRetrieveCashFlowForecastResponse</a></code>
- <code title="get /corporate/treasury/liquidity-positions">client.corporate.treasury.<a href="./src/jocall3/resources/corporate/treasury/treasury.py">retrieve_liquidity_positions</a>() -> <a href="./src/jocall3/types/corporate/treasury_retrieve_liquidity_positions_response.py">TreasuryRetrieveLiquidityPositionsResponse</a></code>

### Sweeping

Methods:

- <code title="post /corporate/treasury/sweeping/rules">client.corporate.treasury.sweeping.<a href="./src/jocall3/resources/corporate/treasury/sweeping.py">configure_rules</a>(\*\*<a href="src/jocall3/types/corporate/treasury/sweeping_configure_rules_params.py">params</a>) -> None</code>
- <code title="post /corporate/treasury/sweeping/execute">client.corporate.treasury.sweeping.<a href="./src/jocall3/resources/corporate/treasury/sweeping.py">execute</a>(\*\*<a href="src/jocall3/types/corporate/treasury/sweeping_execute_params.py">params</a>) -> None</code>

### Pooling

Methods:

- <code title="post /corporate/treasury/liquidity/pooling">client.corporate.treasury.pooling.<a href="./src/jocall3/resources/corporate/treasury/pooling.py">configure</a>(\*\*<a href="src/jocall3/types/corporate/treasury/pooling_configure_params.py">params</a>) -> None</code>

## Cards

Types:

```python
from jocall3.types.corporate import (
    CardListResponse,
    CardIssuePhysicalResponse,
    CardIssueVirtualResponse,
    CardListTransactionsResponse,
)
```

Methods:

- <code title="get /corporate/cards">client.corporate.cards.<a href="./src/jocall3/resources/corporate/cards/cards.py">list</a>(\*\*<a href="src/jocall3/types/corporate/card_list_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/card_list_response.py">CardListResponse</a></code>
- <code title="post /corporate/cards/{cardId}/freeze">client.corporate.cards.<a href="./src/jocall3/resources/corporate/cards/cards.py">freeze</a>(card_id, \*\*<a href="src/jocall3/types/corporate/card_freeze_params.py">params</a>) -> None</code>
- <code title="post /corporate/cards/physical">client.corporate.cards.<a href="./src/jocall3/resources/corporate/cards/cards.py">issue_physical</a>(\*\*<a href="src/jocall3/types/corporate/card_issue_physical_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/card_issue_physical_response.py">CardIssuePhysicalResponse</a></code>
- <code title="post /corporate/cards/virtual">client.corporate.cards.<a href="./src/jocall3/resources/corporate/cards/cards.py">issue_virtual</a>(\*\*<a href="src/jocall3/types/corporate/card_issue_virtual_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/card_issue_virtual_response.py">CardIssueVirtualResponse</a></code>
- <code title="get /corporate/cards/{cardId}/transactions">client.corporate.cards.<a href="./src/jocall3/resources/corporate/cards/cards.py">list_transactions</a>(card_id) -> <a href="./src/jocall3/types/corporate/card_list_transactions_response.py">CardListTransactionsResponse</a></code>

### Controls

Methods:

- <code title="put /corporate/cards/{cardId}/controls">client.corporate.cards.controls.<a href="./src/jocall3/resources/corporate/cards/controls.py">update</a>(card_id, \*\*<a href="src/jocall3/types/corporate/cards/control_update_params.py">params</a>) -> None</code>

## Risk

Types:

```python
from jocall3.types.corporate import RiskRetrieveExposureResponse, RiskRunStressTestResponse
```

Methods:

- <code title="get /corporate/risk/exposure">client.corporate.risk.<a href="./src/jocall3/resources/corporate/risk/risk.py">retrieve_exposure</a>() -> <a href="./src/jocall3/types/corporate/risk_retrieve_exposure_response.py">RiskRetrieveExposureResponse</a></code>
- <code title="post /corporate/risk/stress-test">client.corporate.risk.<a href="./src/jocall3/resources/corporate/risk/risk.py">run_stress_test</a>(\*\*<a href="src/jocall3/types/corporate/risk_run_stress_test_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/risk_run_stress_test_response.py">RiskRunStressTestResponse</a></code>

### Fraud

Types:

```python
from jocall3.types.corporate.risk import FraudAnalyzeResponse
```

Methods:

- <code title="post /corporate/risk/fraud/analyze">client.corporate.risk.fraud.<a href="./src/jocall3/resources/corporate/risk/fraud/fraud.py">analyze</a>(\*\*<a href="src/jocall3/types/corporate/risk/fraud_analyze_params.py">params</a>) -> <a href="./src/jocall3/types/corporate/risk/fraud_analyze_response.py">FraudAnalyzeResponse</a></code>

#### Rules

Types:

```python
from jocall3.types.corporate.risk.fraud import RuleListResponse
```

Methods:

- <code title="post /corporate/risk/fraud/rules">client.corporate.risk.fraud.rules.<a href="./src/jocall3/resources/corporate/risk/fraud/rules.py">create</a>(\*\*<a href="src/jocall3/types/corporate/risk/fraud/rule_create_params.py">params</a>) -> None</code>
- <code title="put /corporate/risk/fraud/rules/{ruleId}">client.corporate.risk.fraud.rules.<a href="./src/jocall3/resources/corporate/risk/fraud/rules.py">update</a>(rule_id, \*\*<a href="src/jocall3/types/corporate/risk/fraud/rule_update_params.py">params</a>) -> None</code>
- <code title="get /corporate/risk/fraud/rules">client.corporate.risk.fraud.rules.<a href="./src/jocall3/resources/corporate/risk/fraud/rules.py">list</a>() -> <a href="./src/jocall3/types/corporate/risk/fraud/rule_list_response.py">RuleListResponse</a></code>

## Governance

### Proposals

Types:

```python
from jocall3.types.corporate.governance import ProposalListResponse
```

Methods:

- <code title="post /corporate/governance/proposals">client.corporate.governance.proposals.<a href="./src/jocall3/resources/corporate/governance/proposals.py">create</a>(\*\*<a href="src/jocall3/types/corporate/governance/proposal_create_params.py">params</a>) -> None</code>
- <code title="get /corporate/governance/proposals">client.corporate.governance.proposals.<a href="./src/jocall3/resources/corporate/governance/proposals.py">list</a>() -> <a href="./src/jocall3/types/corporate/governance/proposal_list_response.py">ProposalListResponse</a></code>
- <code title="post /corporate/governance/proposals/{proposalId}/vote">client.corporate.governance.proposals.<a href="./src/jocall3/resources/corporate/governance/proposals.py">vote</a>(proposal_id, \*\*<a href="src/jocall3/types/corporate/governance/proposal_vote_params.py">params</a>) -> None</code>

## Anomalies

Types:

```python
from jocall3.types.corporate import AnomalyListResponse
```

Methods:

- <code title="get /corporate/anomalies">client.corporate.anomalies.<a href="./src/jocall3/resources/corporate/anomalies.py">list</a>() -> <a href="./src/jocall3/types/corporate/anomaly_list_response.py">AnomalyListResponse</a></code>
- <code title="put /corporate/anomalies/{anomalyId}/status">client.corporate.anomalies.<a href="./src/jocall3/resources/corporate/anomalies.py">update_status</a>(anomaly_id, \*\*<a href="src/jocall3/types/corporate/anomaly_update_status_params.py">params</a>) -> None</code>

# Web3

Types:

```python
from jocall3.types import Web3RetrieveNetworkStatusResponse
```

Methods:

- <code title="get /web3/network/status">client.web3.<a href="./src/jocall3/resources/web3/web3.py">retrieve_network_status</a>() -> <a href="./src/jocall3/types/web3_retrieve_network_status_response.py">Web3RetrieveNetworkStatusResponse</a></code>

## Wallets

Types:

```python
from jocall3.types.web3 import (
    WalletCreateResponse,
    WalletListResponse,
    WalletRetrieveBalancesResponse,
)
```

Methods:

- <code title="post /web3/wallets">client.web3.wallets.<a href="./src/jocall3/resources/web3/wallets.py">create</a>(\*\*<a href="src/jocall3/types/web3/wallet_create_params.py">params</a>) -> <a href="./src/jocall3/types/web3/wallet_create_response.py">WalletCreateResponse</a></code>
- <code title="get /web3/wallets">client.web3.wallets.<a href="./src/jocall3/resources/web3/wallets.py">list</a>() -> <a href="./src/jocall3/types/web3/wallet_list_response.py">WalletListResponse</a></code>
- <code title="post /web3/wallets/connect">client.web3.wallets.<a href="./src/jocall3/resources/web3/wallets.py">connect</a>(\*\*<a href="src/jocall3/types/web3/wallet_connect_params.py">params</a>) -> None</code>
- <code title="get /web3/wallets/{walletId}/balances">client.web3.wallets.<a href="./src/jocall3/resources/web3/wallets.py">retrieve_balances</a>(wallet_id) -> <a href="./src/jocall3/types/web3/wallet_retrieve_balances_response.py">WalletRetrieveBalancesResponse</a></code>

## Transactions

Types:

```python
from jocall3.types.web3 import TransactionSendResponse
```

Methods:

- <code title="post /web3/transactions/bridge">client.web3.transactions.<a href="./src/jocall3/resources/web3/transactions.py">bridge_chain</a>(\*\*<a href="src/jocall3/types/web3/transaction_bridge_chain_params.py">params</a>) -> None</code>
- <code title="post /web3/transactions/initiate">client.web3.transactions.<a href="./src/jocall3/resources/web3/transactions.py">initiate</a>(\*\*<a href="src/jocall3/types/web3/transaction_initiate_params.py">params</a>) -> None</code>
- <code title="post /web3/transactions/send">client.web3.transactions.<a href="./src/jocall3/resources/web3/transactions.py">send</a>(\*\*<a href="src/jocall3/types/web3/transaction_send_params.py">params</a>) -> <a href="./src/jocall3/types/web3/transaction_send_response.py">TransactionSendResponse</a></code>
- <code title="post /web3/transactions/swap">client.web3.transactions.<a href="./src/jocall3/resources/web3/transactions.py">swap_tokens</a>(\*\*<a href="src/jocall3/types/web3/transaction_swap_tokens_params.py">params</a>) -> None</code>

## NFTs

Types:

```python
from jocall3.types.web3 import NFTListResponse
```

Methods:

- <code title="get /web3/nfts">client.web3.nfts.<a href="./src/jocall3/resources/web3/nfts.py">list</a>() -> <a href="./src/jocall3/types/web3/nft_list_response.py">NFTListResponse</a></code>
- <code title="post /web3/nfts/mint">client.web3.nfts.<a href="./src/jocall3/resources/web3/nfts.py">mint</a>(\*\*<a href="src/jocall3/types/web3/nft_mint_params.py">params</a>) -> None</code>

## Contracts

Methods:

- <code title="post /web3/contracts/deploy">client.web3.contracts.<a href="./src/jocall3/resources/web3/contracts.py">deploy</a>(\*\*<a href="src/jocall3/types/web3/contract_deploy_params.py">params</a>) -> None</code>

# Payments

Types:

```python
from jocall3.types import PaymentListResponse
```

Methods:

- <code title="get /payments/{paymentId}">client.payments.<a href="./src/jocall3/resources/payments/payments.py">retrieve</a>(payment_id) -> None</code>
- <code title="get /payments">client.payments.<a href="./src/jocall3/resources/payments/payments.py">list</a>() -> <a href="./src/jocall3/types/payment_list_response.py">PaymentListResponse</a></code>

## Domestic

Methods:

- <code title="post /payments/domestic/ach">client.payments.domestic.<a href="./src/jocall3/resources/payments/domestic.py">send_ach</a>(\*\*<a href="src/jocall3/types/payments/domestic_send_ach_params.py">params</a>) -> None</code>
- <code title="post /payments/domestic/rtp">client.payments.domestic.<a href="./src/jocall3/resources/payments/domestic.py">send_rtp</a>(\*\*<a href="src/jocall3/types/payments/domestic_send_rtp_params.py">params</a>) -> None</code>
- <code title="post /payments/domestic/wire">client.payments.domestic.<a href="./src/jocall3/resources/payments/domestic.py">send_wire</a>(\*\*<a href="src/jocall3/types/payments/domestic_send_wire_params.py">params</a>) -> None</code>

## International

Types:

```python
from jocall3.types.payments import InternationalRetrieveStatusResponse
```

Methods:

- <code title="get /payments/international/{paymentId}/status">client.payments.international.<a href="./src/jocall3/resources/payments/international.py">retrieve_status</a>(payment_id) -> <a href="./src/jocall3/types/payments/international_retrieve_status_response.py">InternationalRetrieveStatusResponse</a></code>
- <code title="post /payments/international/sepa">client.payments.international.<a href="./src/jocall3/resources/payments/international.py">send_sepa</a>(\*\*<a href="src/jocall3/types/payments/international_send_sepa_params.py">params</a>) -> None</code>
- <code title="post /payments/international/swift">client.payments.international.<a href="./src/jocall3/resources/payments/international.py">send_swift</a>(\*\*<a href="src/jocall3/types/payments/international_send_swift_params.py">params</a>) -> None</code>

## Fx

Types:

```python
from jocall3.types.payments import FxRetrieveRatesResponse
```

Methods:

- <code title="post /payments/fx/deals">client.payments.fx.<a href="./src/jocall3/resources/payments/fx.py">book_deal</a>(\*\*<a href="src/jocall3/types/payments/fx_book_deal_params.py">params</a>) -> None</code>
- <code title="post /payments/fx/convert">client.payments.fx.<a href="./src/jocall3/resources/payments/fx.py">convert_currency</a>(\*\*<a href="src/jocall3/types/payments/fx_convert_currency_params.py">params</a>) -> None</code>
- <code title="get /payments/fx/rates">client.payments.fx.<a href="./src/jocall3/resources/payments/fx.py">retrieve_rates</a>(\*\*<a href="src/jocall3/types/payments/fx_retrieve_rates_params.py">params</a>) -> <a href="./src/jocall3/types/payments/fx_retrieve_rates_response.py">FxRetrieveRatesResponse</a></code>

# Sustainability

Types:

```python
from jocall3.types import SustainabilityRetrieveCarbonFootprintResponse
```

Methods:

- <code title="get /sustainability/carbon-footprint">client.sustainability.<a href="./src/jocall3/resources/sustainability/sustainability.py">retrieve_carbon_footprint</a>() -> <a href="./src/jocall3/types/sustainability_retrieve_carbon_footprint_response.py">SustainabilityRetrieveCarbonFootprintResponse</a></code>

## Offsets

Methods:

- <code title="post /sustainability/offsets/purchase">client.sustainability.offsets.<a href="./src/jocall3/resources/sustainability/offsets.py">purchase</a>(\*\*<a href="src/jocall3/types/sustainability/offset_purchase_params.py">params</a>) -> None</code>
- <code title="post /sustainability/offsets/retire">client.sustainability.offsets.<a href="./src/jocall3/resources/sustainability/offsets.py">retire</a>(\*\*<a href="src/jocall3/types/sustainability/offset_retire_params.py">params</a>) -> None</code>

## Impact

Types:

```python
from jocall3.types.sustainability import (
    ImpactListGreenProjectsResponse,
    ImpactRetrievePortfolioAnalysisResponse,
)
```

Methods:

- <code title="get /sustainability/impact/projects">client.sustainability.impact.<a href="./src/jocall3/resources/sustainability/impact.py">list_green_projects</a>(\*\*<a href="src/jocall3/types/sustainability/impact_list_green_projects_params.py">params</a>) -> <a href="./src/jocall3/types/sustainability/impact_list_green_projects_response.py">ImpactListGreenProjectsResponse</a></code>
- <code title="get /sustainability/impact/portfolio">client.sustainability.impact.<a href="./src/jocall3/resources/sustainability/impact.py">retrieve_portfolio_analysis</a>() -> <a href="./src/jocall3/types/sustainability/impact_retrieve_portfolio_analysis_response.py">ImpactRetrievePortfolioAnalysisResponse</a></code>

# Marketplace

Types:

```python
from jocall3.types import MarketplaceListProductsResponse
```

Methods:

- <code title="get /marketplace/products">client.marketplace.<a href="./src/jocall3/resources/marketplace/marketplace.py">list_products</a>() -> <a href="./src/jocall3/types/marketplace_list_products_response.py">MarketplaceListProductsResponse</a></code>

## Offers

Types:

```python
from jocall3.types.marketplace import OfferListResponse
```

Methods:

- <code title="get /marketplace/offers">client.marketplace.offers.<a href="./src/jocall3/resources/marketplace/offers.py">list</a>() -> <a href="./src/jocall3/types/marketplace/offer_list_response.py">OfferListResponse</a></code>
- <code title="post /marketplace/offers/{offerId}/redeem">client.marketplace.offers.<a href="./src/jocall3/resources/marketplace/offers.py">redeem</a>(offer_id) -> None</code>

# Lending

Types:

```python
from jocall3.types import LendingSubmitApplicationResponse
```

Methods:

- <code title="post /lending/applications">client.lending.<a href="./src/jocall3/resources/lending/lending.py">submit_application</a>(\*\*<a href="src/jocall3/types/lending_submit_application_params.py">params</a>) -> <a href="./src/jocall3/types/lending_submit_application_response.py">LendingSubmitApplicationResponse</a></code>

## Applications

Types:

```python
from jocall3.types.lending import ApplicationRetrieveStatusResponse
```

Methods:

- <code title="get /lending/applications/{appId}/status">client.lending.applications.<a href="./src/jocall3/resources/lending/applications.py">retrieve_status</a>(app_id) -> <a href="./src/jocall3/types/lending/application_retrieve_status_response.py">ApplicationRetrieveStatusResponse</a></code>

## Decisions

Types:

```python
from jocall3.types.lending import DecisionRetrieveRationaleResponse
```

Methods:

- <code title="get /lending/decisions/{decisionId}/rationale">client.lending.decisions.<a href="./src/jocall3/resources/lending/decisions.py">retrieve_rationale</a>(decision_id) -> <a href="./src/jocall3/types/lending/decision_retrieve_rationale_response.py">DecisionRetrieveRationaleResponse</a></code>

# Investments

## Portfolios

Types:

```python
from jocall3.types.investments import PortfolioListResponse, PortfolioRebalanceResponse
```

Methods:

- <code title="post /investments/portfolios">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">create</a>(\*\*<a href="src/jocall3/types/investments/portfolio_create_params.py">params</a>) -> None</code>
- <code title="get /investments/portfolios/{portfolioId}">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">retrieve</a>(portfolio_id) -> None</code>
- <code title="put /investments/portfolios/{portfolioId}">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">update</a>(portfolio_id, \*\*<a href="src/jocall3/types/investments/portfolio_update_params.py">params</a>) -> None</code>
- <code title="get /investments/portfolios">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">list</a>(\*\*<a href="src/jocall3/types/investments/portfolio_list_params.py">params</a>) -> <a href="./src/jocall3/types/investments/portfolio_list_response.py">PortfolioListResponse</a></code>
- <code title="post /investments/portfolios/{portfolioId}/rebalance">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">rebalance</a>(portfolio_id, \*\*<a href="src/jocall3/types/investments/portfolio_rebalance_params.py">params</a>) -> <a href="./src/jocall3/types/investments/portfolio_rebalance_response.py">PortfolioRebalanceResponse</a></code>

## Assets

Types:

```python
from jocall3.types.investments import AssetSearchResponse
```

Methods:

- <code title="get /investments/assets/search">client.investments.assets.<a href="./src/jocall3/resources/investments/assets.py">search</a>(\*\*<a href="src/jocall3/types/investments/asset_search_params.py">params</a>) -> <a href="./src/jocall3/types/investments/asset_search_response.py">AssetSearchResponse</a></code>

## Performance

Types:

```python
from jocall3.types.investments import PerformanceRetrieveHistoricalResponse
```

Methods:

- <code title="get /investments/performance/historical">client.investments.performance.<a href="./src/jocall3/resources/investments/performance.py">retrieve_historical</a>(\*\*<a href="src/jocall3/types/investments/performance_retrieve_historical_params.py">params</a>) -> <a href="./src/jocall3/types/investments/performance_retrieve_historical_response.py">PerformanceRetrieveHistoricalResponse</a></code>

# System

## Status

Types:

```python
from jocall3.types.system import StatusRetrieveResponse
```

Methods:

- <code title="get /system/status">client.system.status.<a href="./src/jocall3/resources/system/status.py">retrieve</a>() -> <a href="./src/jocall3/types/system/status_retrieve_response.py">StatusRetrieveResponse</a></code>

## Webhooks

Types:

```python
from jocall3.types.system import WebhookListResponse
```

Methods:

- <code title="post /system/webhooks">client.system.webhooks.<a href="./src/jocall3/resources/system/webhooks.py">create</a>(\*\*<a href="src/jocall3/types/system/webhook_create_params.py">params</a>) -> None</code>
- <code title="get /system/webhooks">client.system.webhooks.<a href="./src/jocall3/resources/system/webhooks.py">list</a>() -> <a href="./src/jocall3/types/system/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /system/webhooks/{webhookId}">client.system.webhooks.<a href="./src/jocall3/resources/system/webhooks.py">delete</a>(webhook_id) -> None</code>

## AuditLogs

Types:

```python
from jocall3.types.system import AuditLogListResponse
```

Methods:

- <code title="get /system/audit-logs">client.system.audit_logs.<a href="./src/jocall3/resources/system/audit_logs.py">list</a>(\*\*<a href="src/jocall3/types/system/audit_log_list_params.py">params</a>) -> <a href="./src/jocall3/types/system/audit_log_list_response.py">AuditLogListResponse</a></code>

## Sandbox

Types:

```python
from jocall3.types.system import SandboxForceErrorResponse
```

Methods:

- <code title="post /system/sandbox/simulate-error">client.system.sandbox.<a href="./src/jocall3/resources/system/sandbox.py">force_error</a>(\*\*<a href="src/jocall3/types/system/sandbox_force_error_params.py">params</a>) -> <a href="./src/jocall3/types/system/sandbox_force_error_response.py">SandboxForceErrorResponse</a></code>
- <code title="post /system/sandbox/reset">client.system.sandbox.<a href="./src/jocall3/resources/system/sandbox.py">reset</a>() -> None</code>

## Verification

Methods:

- <code title="post /system/verification/biometric-comparison">client.system.verification.<a href="./src/jocall3/resources/system/verification.py">compare_biometrics</a>(\*\*<a href="src/jocall3/types/system/verification_compare_biometrics_params.py">params</a>) -> None</code>
- <code title="post /system/verification/document">client.system.verification.<a href="./src/jocall3/resources/system/verification.py">verify_document</a>(\*\*<a href="src/jocall3/types/system/verification_verify_document_params.py">params</a>) -> None</code>

## Notifications

Types:

```python
from jocall3.types.system import NotificationListTemplatesResponse
```

Methods:

- <code title="get /system/notifications/templates">client.system.notifications.<a href="./src/jocall3/resources/system/notifications.py">list_templates</a>() -> <a href="./src/jocall3/types/system/notification_list_templates_response.py">NotificationListTemplatesResponse</a></code>
- <code title="post /system/notifications/push">client.system.notifications.<a href="./src/jocall3/resources/system/notifications.py">send_push</a>(\*\*<a href="src/jocall3/types/system/notification_send_push_params.py">params</a>) -> None</code>

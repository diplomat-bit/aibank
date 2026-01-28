# Users

Types:

```python
from jocall3.types import UserLoginResponse, UserRegisterResponse
```

Methods:

- <code title="post /users/login">client.users.<a href="./src/jocall3/resources/users/users.py">login</a>(\*\*<a href="src/jocall3/types/user_login_params.py">params</a>) -> <a href="./src/jocall3/types/user_login_response.py">UserLoginResponse</a></code>
- <code title="post /users/register">client.users.<a href="./src/jocall3/resources/users/users.py">register</a>(\*\*<a href="src/jocall3/types/user_register_params.py">params</a>) -> <a href="./src/jocall3/types/user_register_response.py">UserRegisterResponse</a></code>

## Me

Types:

```python
from jocall3.types.users import MeRetrieveResponse, MeUpdateResponse
```

Methods:

- <code title="get /users/me">client.users.me.<a href="./src/jocall3/resources/users/me/me.py">retrieve</a>() -> <a href="./src/jocall3/types/users/me_retrieve_response.py">MeRetrieveResponse</a></code>
- <code title="put /users/me">client.users.me.<a href="./src/jocall3/resources/users/me/me.py">update</a>(\*\*<a href="src/jocall3/types/users/me_update_params.py">params</a>) -> <a href="./src/jocall3/types/users/me_update_response.py">MeUpdateResponse</a></code>

### Preferences

Types:

```python
from jocall3.types.users.me import PreferenceRetrieveResponse, PreferenceUpdateResponse
```

Methods:

- <code title="get /users/me/preferences">client.users.me.preferences.<a href="./src/jocall3/resources/users/me/preferences.py">retrieve</a>() -> <a href="./src/jocall3/types/users/me/preference_retrieve_response.py">PreferenceRetrieveResponse</a></code>
- <code title="put /users/me/preferences">client.users.me.preferences.<a href="./src/jocall3/resources/users/me/preferences.py">update</a>(\*\*<a href="src/jocall3/types/users/me/preference_update_params.py">params</a>) -> <a href="./src/jocall3/types/users/me/preference_update_response.py">PreferenceUpdateResponse</a></code>

### Devices

Types:

```python
from jocall3.types.users.me import DeviceListResponse
```

Methods:

- <code title="get /users/me/devices">client.users.me.devices.<a href="./src/jocall3/resources/users/me/devices.py">list</a>(\*\*<a href="src/jocall3/types/users/me/device_list_params.py">params</a>) -> <a href="./src/jocall3/types/users/me/device_list_response.py">DeviceListResponse</a></code>

### Biometrics

Types:

```python
from jocall3.types.users.me import BiometricRetrieveStatusResponse, BiometricVerifyResponse
```

Methods:

- <code title="get /users/me/biometrics">client.users.me.biometrics.<a href="./src/jocall3/resources/users/me/biometrics.py">retrieve_status</a>() -> <a href="./src/jocall3/types/users/me/biometric_retrieve_status_response.py">BiometricRetrieveStatusResponse</a></code>
- <code title="post /users/me/biometrics/verify">client.users.me.biometrics.<a href="./src/jocall3/resources/users/me/biometrics.py">verify</a>(\*\*<a href="src/jocall3/types/users/me/biometric_verify_params.py">params</a>) -> <a href="./src/jocall3/types/users/me/biometric_verify_response.py">BiometricVerifyResponse</a></code>

# Accounts

Types:

```python
from jocall3.types import AccountRetrieveResponse, AccountListResponse, AccountLinkResponse
```

Methods:

- <code title="get /accounts/{accountId}/details">client.accounts.<a href="./src/jocall3/resources/accounts/accounts.py">retrieve</a>(account_id) -> <a href="./src/jocall3/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="get /accounts/me">client.accounts.<a href="./src/jocall3/resources/accounts/accounts.py">list</a>(\*\*<a href="src/jocall3/types/account_list_params.py">params</a>) -> <a href="./src/jocall3/types/account_list_response.py">AccountListResponse</a></code>
- <code title="post /accounts/link">client.accounts.<a href="./src/jocall3/resources/accounts/accounts.py">link</a>(\*\*<a href="src/jocall3/types/account_link_params.py">params</a>) -> <a href="./src/jocall3/types/account_link_response.py">AccountLinkResponse</a></code>

## Transactions

Types:

```python
from jocall3.types.accounts import TransactionListPendingResponse
```

Methods:

- <code title="get /accounts/{accountId}/transactions/pending">client.accounts.transactions.<a href="./src/jocall3/resources/accounts/transactions.py">list_pending</a>(account_id, \*\*<a href="src/jocall3/types/accounts/transaction_list_pending_params.py">params</a>) -> <a href="./src/jocall3/types/accounts/transaction_list_pending_response.py">TransactionListPendingResponse</a></code>

## Statements

Types:

```python
from jocall3.types.accounts import StatementListResponse
```

Methods:

- <code title="get /accounts/{accountId}/statements">client.accounts.statements.<a href="./src/jocall3/resources/accounts/statements.py">list</a>(account_id, \*\*<a href="src/jocall3/types/accounts/statement_list_params.py">params</a>) -> <a href="./src/jocall3/types/accounts/statement_list_response.py">StatementListResponse</a></code>

## Overdraft

Types:

```python
from jocall3.types.accounts import OverdraftUpdateResponse, OverdraftGetResponse
```

Methods:

- <code title="put /accounts/{accountId}/overdraft-settings">client.accounts.overdraft.<a href="./src/jocall3/resources/accounts/overdraft.py">update</a>(account_id, \*\*<a href="src/jocall3/types/accounts/overdraft_update_params.py">params</a>) -> <a href="./src/jocall3/types/accounts/overdraft_update_response.py">OverdraftUpdateResponse</a></code>
- <code title="get /accounts/{accountId}/overdraft-settings">client.accounts.overdraft.<a href="./src/jocall3/resources/accounts/overdraft.py">get</a>(account_id) -> <a href="./src/jocall3/types/accounts/overdraft_get_response.py">OverdraftGetResponse</a></code>

# Transactions

Types:

```python
from jocall3.types import (
    TransactionRetrieveResponse,
    TransactionListResponse,
    TransactionAddNotesResponse,
    TransactionCategorizeResponse,
)
```

Methods:

- <code title="get /transactions/{transactionId}">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">retrieve</a>(transaction_id) -> <a href="./src/jocall3/types/transaction_retrieve_response.py">TransactionRetrieveResponse</a></code>
- <code title="get /transactions">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">list</a>(\*\*<a href="src/jocall3/types/transaction_list_params.py">params</a>) -> <a href="./src/jocall3/types/transaction_list_response.py">TransactionListResponse</a></code>
- <code title="put /transactions/{transactionId}/notes">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">add_notes</a>(transaction_id, \*\*<a href="src/jocall3/types/transaction_add_notes_params.py">params</a>) -> <a href="./src/jocall3/types/transaction_add_notes_response.py">TransactionAddNotesResponse</a></code>
- <code title="put /transactions/{transactionId}/categorize">client.transactions.<a href="./src/jocall3/resources/transactions/transactions.py">categorize</a>(transaction_id, \*\*<a href="src/jocall3/types/transaction_categorize_params.py">params</a>) -> <a href="./src/jocall3/types/transaction_categorize_response.py">TransactionCategorizeResponse</a></code>

## Recurring

Types:

```python
from jocall3.types.transactions import RecurringListResponse
```

Methods:

- <code title="get /transactions/recurring">client.transactions.recurring.<a href="./src/jocall3/resources/transactions/recurring.py">list</a>(\*\*<a href="src/jocall3/types/transactions/recurring_list_params.py">params</a>) -> <a href="./src/jocall3/types/transactions/recurring_list_response.py">RecurringListResponse</a></code>

## Insights

Types:

```python
from jocall3.types.transactions import InsightGetTrendsResponse
```

Methods:

- <code title="get /transactions/insights/spending-trends">client.transactions.insights.<a href="./src/jocall3/resources/transactions/insights.py">get_trends</a>() -> <a href="./src/jocall3/types/transactions/insight_get_trends_response.py">InsightGetTrendsResponse</a></code>

# Budgets

Types:

```python
from jocall3.types import BudgetRetrieveResponse, BudgetUpdateResponse, BudgetListResponse
```

Methods:

- <code title="get /budgets/{budgetId}">client.budgets.<a href="./src/jocall3/resources/budgets.py">retrieve</a>(budget_id) -> <a href="./src/jocall3/types/budget_retrieve_response.py">BudgetRetrieveResponse</a></code>
- <code title="put /budgets/{budgetId}">client.budgets.<a href="./src/jocall3/resources/budgets.py">update</a>(budget_id, \*\*<a href="src/jocall3/types/budget_update_params.py">params</a>) -> <a href="./src/jocall3/types/budget_update_response.py">BudgetUpdateResponse</a></code>
- <code title="get /budgets">client.budgets.<a href="./src/jocall3/resources/budgets.py">list</a>(\*\*<a href="src/jocall3/types/budget_list_params.py">params</a>) -> <a href="./src/jocall3/types/budget_list_response.py">BudgetListResponse</a></code>

# Investments

## Portfolios

Methods:

- <code title="get /investments/portfolios/{portfolioId}">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">retrieve</a>(portfolio_id) -> object</code>
- <code title="put /investments/portfolios/{portfolioId}">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">update</a>(portfolio_id) -> object</code>
- <code title="get /investments/portfolios">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">list</a>(\*\*<a href="src/jocall3/types/investments/portfolio_list_params.py">params</a>) -> object</code>
- <code title="post /investments/portfolios/{portfolioId}/rebalance">client.investments.portfolios.<a href="./src/jocall3/resources/investments/portfolios.py">rebalance</a>(portfolio_id) -> object</code>

## Assets

Methods:

- <code title="get /investments/assets/search">client.investments.assets.<a href="./src/jocall3/resources/investments/assets.py">search</a>(\*\*<a href="src/jocall3/types/investments/asset_search_params.py">params</a>) -> object</code>

# AI

## Advisor

Methods:

- <code title="post /ai/advisor/chat">client.ai.advisor.<a href="./src/jocall3/resources/ai/advisor/advisor.py">chat</a>(\*\*<a href="src/jocall3/types/ai/advisor_chat_params.py">params</a>) -> object</code>
- <code title="get /ai/advisor/chat/history">client.ai.advisor.<a href="./src/jocall3/resources/ai/advisor/advisor.py">history</a>(\*\*<a href="src/jocall3/types/ai/advisor_history_params.py">params</a>) -> object</code>

### Tools

Methods:

- <code title="get /ai/advisor/tools">client.ai.advisor.tools.<a href="./src/jocall3/resources/ai/advisor/tools.py">list</a>(\*\*<a href="src/jocall3/types/ai/advisor/tool_list_params.py">params</a>) -> object</code>

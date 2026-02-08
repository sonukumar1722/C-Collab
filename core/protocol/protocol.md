## Execute request (Input message)
This is what client sends.
```json
{
  "type": "execute_request",
  "request_id": "uuid-1234",
  "session_id": "session-abc",
  "language": "cpp",
  "code": "int x = 10;",
  "timeout": 3
}
```
Semantics:
- `request_id` -> trac this execution
- `session_id` -> notebook session
- `anguage` -> fututre proof
- `timeout` -> per-cell  control

## Execute response (Final Result)
Sent once per execution
```json
{
  "type": "execute_response",
  "request_id": "uuid-1234",
  "execution_count": 1,
  "status": "ok",
  "stdout": "",
  "stderr": ""
}
```
Possible `status`
- `ok`
- `error`
- `timeout`
- `interrupted`


## Stream output 
Used when output is long or real-time.
```json
{
  "type": "stream_output",
  "request_id": "uuid-1234",
  "stream": "stdout",
  "data": "Processing...\n"
}
```
This is how:
- `cout` appears live

## Error message (Hard Failures)
Used when execution cannot even start.
```json
{
  "type": "error",
  "request_id": "uuid-1234",
  "error_type": "kernel_error",
  "message": "Kernel not running"
}
```
## Status message (Kernel Lifecycle)
Kernel -> client event
```json
{
  "type": "status",
  "session_id": "session-abc",
  "state": "busy"
}
```
States:
- `starting`
- `idle`
- `busy`
- `dead`

## Interrupt & Restart request
### Inturrupt
```json
{
  "type": "interrupt",
  "session_id": "session-abc"
}
```
### Restart
```json
{
  "type": "restart",
  "session_id": "session-abc"
}
```

## Dry Flow (E2E)
```text
Client
  |
  | execute_request
  v
NotebookSession
  |
  | -> KernelManager.execute()
  v
CppKernel (Cling)
  |
  | output
  v
execute_response
```
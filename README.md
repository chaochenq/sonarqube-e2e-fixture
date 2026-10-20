# sonarqube-e2e-fixture

A test fixture for Trent's SonarQube Cloud connector. Every weakness here is
planted on purpose and made up. Do not deploy this code.

- `app/` (Python): a SQL injection reached from a request parameter, a weak
  hash, a debug flag, an insecure random token, a cleartext URL, plus style and
  reliability noise with no security impact.
- `web/` (JavaScript): `eval` of user input and an insecure random token.
- `java/`: SQL built by string concatenation and a weak cipher.
- `e2e/change.json`: the one planted issue the end-to-end run fixes and reverts.

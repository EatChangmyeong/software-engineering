## Create account

* Actor: user
* Actor's goal: select whether user is patient or doctor and create account with his/her information

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Form to accept user's personal information required for signup | D | SignUpForm |
| Check if the given account information is valid | D | AccountInfoValidator |
| Database for account information of all users | K | UserDatabase |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Create a new account according to provided information | D | AccountGenerator |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| SignUpForm - Controller | SignUpForm requests account creation with given user information to Controller | conveys requests |
| Controller - AccountInfoValidator | Controller sends user information to AccountInfoValidator to validate the given information | requests validation |
| AccountInfoValidator - UserDatabase | AccountInfoValidator retrieves registered user ids to avoid collision | retrieves ids |
| Controller - AccountGenerator | Controller conveys user data to AccountGenerator to create new account according to given information | conveys requests |
| AccountGenerator - UserDatabase | AccountGenerator inserts a new user record into UserDatabase | inserts data to |
| AccountGenerator - PasswordStorage | AccountGenerator inserts an encrypted password data associated to a user into PasswordStorage | inserts data to |

## Login

* Actor: user
* Actor's goal: log in with user's id and password

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Form to input user's id and password | D | SignInForm |
| Verify whether the provided password is correct | D | PasswordChecker |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Review recent login failure and block suspicious login attempts | D | SignInBlocker |
| Log for recent failed login attempts | K | FailedSignInLog |
| Grant a user who provided correct password signed-in state | D | UserCredential |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| SignInForm - Controller | SignInForm requests user login with given id and password to Controller | conveys requests |
| Controller - PasswordChecker | Controller sends id and password pair to PasswordChecker for verification | requests verification |
| PasswordChecker - PasswordStorage | PasswordChecker retrieves password data linked to given id (if any) for comparison | retrieves password |
| PasswordChecker - SignInBlocker | PasswordChecker checks if the specified user is in the blocked state | retrieves data |
| Controller - FailedSignInLog | Controller logs a login attempt to FailedSignInLog if the password does not match or clears failed attempts | logs |
| Controller - UserCredential | Controller requests UserCredential to issue a user logged in state | requests certification |

## View/change information

* Actor: patient and doctor
* Actor's goal: view or change personal information

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Render a user's information tied to his/her account | D | UserPageRenderer |
| Form to accept new information to be changed | D | AccountUpdateForm |
| Check if the given account information is valid | D | AccountInfoValidator |
| Database for account information of all users | K | UserDatabase |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Update an account's information according to request | D | AccountUpdater |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| Controller - UserDatabase | Controller retrieves account information from UserDatabase | retrieves data |
| Controller - UserPageRenderer | Controller sends gathered account information to UserPageRenderer for displaying | conveys data |
| AccountUpdateForm - Controller | AccountUpdateForm sends update request to controller along with information to be changed | conveys request |
| Controller - AccountInfoValidator | Controller sends user information to AccountInfoValidator to validate the given information | requests validation |
| AccountInfoValidator - UserDatabase | AccountInfoValidator retrieves registered user ids to avoid collision | retrieves ids |
| Controller - AccountUpdater | Controller requests to update some details for an account | conveys request |
| AccountUpdater - UserDatabase | AccountUpdater updates specified user details on UserDatabase | updates data |
| AccountUpdater - PasswordStorage | AccountUpdater stores the new password in PasswordStorage | updates data |

## Logout

* Actor: patient and doctor
* Actor's goal: log out

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Revoke a user's signed-in state | D | RevokeUserCredential |

### Associations

None worth mentioning.

## View medical history

* Actor: doctor
* Actor's goal: view medical history of his/her patient

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Database for medical history of each doctor | K | HistoryDatabase |
| Render the list of medical history on screen | D | HistoryListRenderer |
| Render one instance of medical history on screen | D | HistoryRenderer |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| Controller - HistoryDatabase | Controller retrieves required history data from HistoryDatabase | retrieves data |
| Controller - HistoryListRenderer | Controller sends a list of medical history for display | conveys data |
| Controller - HistoryRenderer | Controller sends a detailed collection of medical history data for display | conveys data |

## Notify patient

* Actor: system
* Actor's goal: notify the patient if their appointment is cancelled or rescheduled by doctor

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Store recent notifications sent to each user | K | NotificationStorage |
| Show a list of notifications for current user | D | NotificationBoard |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| Controller - NotificationStore | Controller retrieves a list of notifications current user has received | retrieves data |
| Controller - NotificationBoard | Controller sends a list of notifications for display | conveys data |

## Block user login

* Actor: system
* Actor's goal: forbid a user to log in for 24 hours if he/she fails to log in more than 5 times

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Review recent login failure and block suspicious login attempts | D | SignInBlocker |
| Log for recent failed login attempts | K | FailedSignInLog |
| Revoke login blockage after 24 hours | D | SignInBlockTimer |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| SignInBlocker - FailedSignInLog | SignInBlocker receives recent history of login attempts for review | retrieves data |
| SignInBlocker - SignInBlockTimer | SignInBlocker sets a 24-hour timer to revoke login blockage | sets timer |

## Find id/password

* Actor: user
* Actor's goal: find his/her id and password with questions to verify him/her, if he/she forgot them

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Form to accept user's personal information for comparison | D | FindPasswordForm |
| Verify whether the provided information is correct | D | FindPasswordChecker |
| Database for account information of all users | K | UserDatabase |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Display the corresponding user's id or password | D | PasswordFoundPage |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| FindPasswordForm - Controller | FindPasswordForm requests account match along with personal information | conveys request |
| Controller - FindPasswordChecker | Controller sends personal information to FindPasswordChecker for verification | requests verification |
| FindPasswordChecker - UserDatabase | FindPasswordChecker retrieves matching user data from UserDatabase for comparison | retrieves data |
| Controller - UserDatabase | Controller retrieves specified user's id for recovery | retrieves id |
| Controller - PasswordStorage* | Controller retrieves specified user's password for recovery | retrieves password |
| Controller - PasswordStorage* | Controller updates specified user's password | updates password |
| Controller - PasswordFoundPage | Controller sends requested data (id or password) to PasswordFoundPage for display | conveys data |

\* tentative; only one association will be selected

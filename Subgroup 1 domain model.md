## Create account

* Actor: user
* Actor's goal: select whether user is patient or doctor and create account with his/her information

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Form to accept user's personal information required for signup | D | SignUpForm |
| Check if the given account information is valid | D | AccountInfoValidator |
| Database for account information of all users | K | UserDatabase |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Create a new account according to provided information | D | AccountGenerator |

## Login

* Actor: user
* Actor's goal: log in with user's id and password

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Form to input user's id and password | D | SignInForm |
| Verify whether the provided password is correct | D | PasswordChecker |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Grant a user who provided correct password signed-in state | D | UserCredential |

## View/change information

* Actor: patient and doctor
* Actor's goal: view or change personal information

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Render a user's information tied to his/her account | D | UserPageRenderer |
| Form to accept new information to be changed | D | AccountUpdateForm |
| Check if the given account information is valid | D | AccountInfoValidator |
| Database for account information of all users | K | UserDatabase |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Update an account's information according to request | D | AccountUpdater |

## Logout

* Actor: patient and doctor
* Actor's goal: log out

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Revoke a user's signed-in state | D | RevokeUserCredential |

## View medical history

* Actor: doctor
* Actor's goal: view medical history of his/her patient

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Retrieve medical history associated to that doctor | D | HistoryReader |
| Database for medical history of each doctor | K | HistoryDatabase |
| Render the list of medical history on screen | D | HistoryListRenderer |
| Render one instance of medical history on screen | D | HistoryRenderer |

## Notify patient

* Actor: system
* Actor's goal: notify the patient if their appointment is cancelled or rescheduled by doctor

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Store recent notifications sent to each user | K | NotificationStore |
| Check if current user has any unread notifications | D | NotificationReader |
| Show a list of notifications for current user | D | NotificationBoard |

## Block user login

* Actor: system
* Actor's goal: forbid a user to log in for 24 hours if he/she fails to log in more than 5 times

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Log for recent failed login attempts | K | FailedSignInLog |
| Review recent login failure and block suspicious login attempts | D | SignInBlocker |
| Revoke login blockage after 24 hours | D | SignInBlockTimer |

## Find id/password

* Actor: user
* Actor's goal: find his/her id and password with questions to verify him/her, if he/she forgot them

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Form to accept user's personal information for comparison | D | FindPasswordForm |
| Verify whether the provided information is correct | D | FindPasswordChecker |
| Database for account information of all users | K | UserDatabase |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Display the corresponding user's id or password | D | PasswordFoundPage |
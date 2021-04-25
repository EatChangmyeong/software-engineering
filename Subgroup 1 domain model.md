## Create account

* Actor: user
* Actor's goal: select whether user is patient or doctor and create account with his/her information

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Form to accept user's personal information required for signup | K | SignUpForm |
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

### Attributes

* **SignUpForm**
	* User type: determines whether the new user is doctor or patient
	* Personal information: describes account information for new user
* **AccountGenerator**
	* User type *(copied from SignUpForm)*
	* Personal information *(copied from SignUpForm)*

## Login

* Actor: user
* Actor's goal: log in with user's id and password

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Form to input user's id and password | K | SignInForm |
| Verify whether the provided password is correct | D | PasswordChecker |
| Container for encrypted passwords associated with users | K | PasswordStorage |
| Grant a user who provided correct password signed-in state | D | UserCredential |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| SignInForm - Controller | SignInForm requests user login with given id and password to Controller | conveys requests |
| Controller - PasswordChecker | Controller sends id and password pair to PasswordChecker for verification | requests verification |
| PasswordChecker - PasswordStorage | PasswordChecker retrieves password data linked to given id (if any) for comparison | retrieves password |
| Controller - UserCredential | Controller requests UserCredential to issue a user logged in state | requests certification |

### Attributes

* **SignInForm**
	* Id: used to determine which user is trying to sign in
	* Password: used to confirm the user identity
* **UserCredential**
	* Id *(copied from SignInForm)*

## View/change information

* Actor: patient and doctor
* Actor's goal: view or change personal information

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Render a user's information tied to his/her account | D | UserPageRenderer |
| Form to accept new information to be changed | K | AccountUpdateForm |
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

### Attributes

* **UserPageRenderer**
	* Personal information: describes account information for current user
* **AccountUpdateForm**
	* Personal information *(copied from UserPageRenderer)*: describes account information to be changed
* **AccountUpdater**
	* Personal information *(copied from AccountUpdateForm)*

## Logout

* Actor: patient and doctor
* Actor's goal: log out

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Revoke a user's signed-in state | D | RevokeUserCredential |

### Associations

None worth mentioning.

### Attributes

* **RevokeUserCredential**
	* Id: used to determine which user is trying to sign out

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

### Attributes

* **Controller**
	* User's identity: used to determine which history instances are associated to the current user
* **HistoryListRenderer**
	* History list: list of medical history for the current user
* **HistoryRenderer**
	* History instance: a medical record the user is interested in

## Notify patient

* Actor: system
* Actor's goal: notify the patient if their appointment is cancelled or rescheduled by doctor

| Responsibility Description | Type | Concept Name |
| - | - | - |
| Coordinate actions all concepts associated with this use case | D | Controller |
| Store recent notifications sent to each user | K | NotificationStore |
| Show a list of notifications for current user | D | NotificationBoard |

### Associations

| Concept pair | Association Description | Association Name |
| - | - | - |
| Controller - NotificationStore | Controller retrieves a list of notifications current user has received | retrieves data |
| Controller - NotificationBoard | Controller sends a list of notifications for display | conveys data |

### Attributes

* **Controller**
	* User's identity: used to determine which notifications the current user has received
* **NotificationBoard**
	* Notification list: list of important notices for the current user
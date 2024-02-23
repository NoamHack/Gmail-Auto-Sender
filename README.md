# **סקריפט פייתון לשליחת דוא"ל באופן אוטומטי** 🤖🤖🤖

## הקדמה:

סקריפט פייתון זה מיועד לשליחת דוא"לים באופן אוטומטי במרווחים זמניים מוגדרים. הוא משתמש בספריות `smtplib` לתקשורת ו־`email` להרכבת דוא"ל ושליחה. המשתמשים יכולים להגדיר את הסקריפט עם פרטי חשבון הדוא"ל שלהם וקבצי דואר אלקטרוני מידע משתמש.

## דרישות:
לפני הרצת הסקריפט, ודאו שפייתון מותקן במחשב המקומי שלכם. בנוסף, יש לכם חשבון Gmail פעיל עם ההרשאות הנדרשות לשליחת דואר באמצעות SMTP.

## כדי להפעיל את הקוד:
   הורידו את סקריפט הפייתון שסופק או צרו קובץ פייתון חדש והדביקו בו את תוכן הסקריפט.
   וודאו שהספריות הנדרשות (`smtplib`, `time`, `email`, `mimetypes`, `os`) מותקנות. אם לא, התקינו אותם באמצעות הפקודה הבאה:

   ```
   pip install secure-smtplib
   ```
   פתחו את הסקריפט בעורך טקסט ובצעו את השינויים הבאים:
   החליפו את `YOUR_EMAIL` בכתובת הדוא"ל האישית שלכם.
   החליפו את `YOUR_PASSWORD` בסיסמת האפליקציה של Gmail אם הפיכת הגישה דו־שלבית מופעלת.
שנו את `YOUR_SUBJECT`, `FROM_EMAIL`, `TO_EMAIL`, `EMAIL_BODY`, ו־`FILE_PATH` (במידה ואתם לא רוצים לצרף קבצים תמחקו את הstring) בפונקצית `main` בהתאם לפרטים שלכם.

## הרצת הסקריפט:
כדי להריץ את הסקריפט על מחשב מקומי:
   פתחו את מסך הפקודות או פקודה רגילה ונווטו לתיקייה שבה נשמר הסקריפט.
   הריצו את הסקריפט על ידי הפקודה הבאה:

   ```
   python email_sender.py
   ```

## פונקציונליות:
לאחר הפעלת הסקריפט, הוא ישלח דוא"ל עם הפרטים והצרופות שצוינו במרווחים קבועים, כפי שמוגדר במשתנה `send_interval` (האימייל שולח את האימייל במרווח של שעה, יחידות המידה הם שניות).


15HXlNem15zXl9eUINec15fXpNeV16gg15zXnteZ15jXkSAoIDo=

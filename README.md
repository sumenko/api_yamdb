# Спринт 11. Коллективный проект api_yamdb

### Описание проекта

Проект **YaMDb** собирает **отзывы** (**Review**) пользователей на **произведения** (**Title**). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список **категорий** (**Category**) может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Сами произведения в **YaMDb** не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть **произведения**: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (**Review**) и выставляют произведению **рейтинг** (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается **средняя оценка произведения**.

### Работа с API

Описание API для работы с базой отзывов **yamdb** доступно по адресу `/redoc`

### Пользовательские роли

- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь (**`user`**)**— может читать всё, как и **Аноним**, дополнительно может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять **свои** отзывы и комментарии.
- **Модератор (**`moderator`**)** — те же права, что и у **Аутентифицированного пользователя** плюс право удалять и редактировать **любые** отзывы и комментарии.
- **Администратор (**`admin`**)** — полные права на управление проектом и всем его содержимым. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- **Администратор Django** — те же права, что и у роли **Администратор**.

### Алгоритм регистрации пользователей

1. Пользователь отправляет POST-запрос с параметром `email` на `/api/v1/auth/email/`.
2. **YaMDB** отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес `email` .
3. Пользователь отправляет POST-запрос с параметрами `email` и `confirmation_code` на `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).

### Ресурсы API **YaMDb**

- Ресурс **AUTH:** аутентификация.
- Ресурс **USERS:** пользователи.
- Ресурс **TITLES:** произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- Ресурс **CATEGORIES:** категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс **GENRES**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс **REVIEWS:** отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс **COMMENTS:** комментарии к отзывам. Комментарий привязан к определённому отзыву.

Каждый ресурс описан в документации: указаны эндпойнты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры, если это необходимо.

## Связанные данные и каскадное удаление

При удалении объекта пользователя **User** должны удаляться все отзывы и комментарии этого пользователя (вместе с оценками-рейтингами).

При удалении объекта произведения **Title** должны удаляться все отзывы к этому произведению и комментарии к ним.

При удалении объекта категории **Category** не удалять связанные с этой категорией произведения (**Title)**.

При удалении объекта жанра **Genre** не удалять связанные с этим жанром произведения (**Title)**.

При удалении объекта отзыва **Review** должны быть удалены все комментарии к этому отзыву.

## База данных

Предварительный импорт данных можно сделать через форму в панели администратора `/admin` (файлы `.csv`, `.xls`, `.json` и другие)


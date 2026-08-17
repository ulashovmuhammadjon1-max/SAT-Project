# SAT Tutor AI Setup Guide

The SATForge app now includes a free SAT tutor powered by Google's Gemini API.

## 🎯 Features

- **Free tier**: 5 tutor requests per user per day
- **Smart hints**: AI provides guidance without giving away answers
- **Rate-limited**: Prevents abuse and keeps costs to zero for small user bases
- **Available in Practice**: Students can ask for help on any practice question

## 🔧 Setup Steps

### 1. Get a Gemini API Key (Free)

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Get API Key" → "Create API Key in new project"
3. Copy your API key (starts with `AI...`)

### 2. Add to Environment Variables

Add to your `.env.local` (local dev) or production environment:

```bash
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

**Important**: Never commit this to git. It should only be in:
- `.env.local` (local dev, not committed)
- Environment variables on your hosting platform (Vercel, etc.)

### 3. Apply Database Migration

Before running the app, apply the migration to add the `TutorUsage` table:

**Local development:**
```bash
npx prisma migrate dev --name tutor_usage
```

**Production (using Neon HTTP API):**
The migration file is at `prisma/migrations/manual/013_tutor_usage.sql`. Apply it using:
```bash
psql $DATABASE_URL < prisma/migrations/manual/013_tutor_usage.sql
```

Or via Neon dashboard → SQL Editor.

### 4. Start the App

```bash
npm run dev
```

Visit `/practice/[questionId]` and click "Get Help" to test the tutor.

---

## 💡 How It Works

1. **Student clicks "Get Help"** on a practice question
2. **Rate limit check**: Server checks if student has requests left today
3. **API call**: If allowed, question is sent to Gemini with a tutor prompt
4. **Response**: AI provides a 2-3 sentence hint or guidance
5. **Tracking**: Usage is logged in `TutorUsage` table for daily limit enforcement

## 📊 Rate Limiting

- **Limit**: 5 requests per user per day
- **Resets**: At UTC midnight (00:00 UTC)
- **Cost**: ~Free for small user bases (Gemini free tier: 15 requests/min, generous quota)

To adjust the limit, edit `src/server/actions/student/sat-tutor.ts`:
```typescript
const DAILY_LIMIT = 5; // Change this number
```

## 🚀 Production Deployment

### Vercel

1. Go to Project Settings → Environment Variables
2. Add `GEMINI_API_KEY` with your API key
3. Redeploy
4. Apply the migration to your production database (Neon dashboard)

### Other Platforms

1. Set `GEMINI_API_KEY` in your platform's env var config
2. Apply the migration SQL to your database
3. Deploy as normal

---

## ⚠️ Troubleshooting

### "GEMINI_API_KEY not configured"
- Check that your `.env.local` or environment variables include the key
- Restart the dev server after adding the variable

### "TutorUsage relation not found" 
- You haven't run the migration yet
- Run `npx prisma migrate dev --name tutor_usage`

### Rate limit shows 0 requests every time
- Restart the app if you just added the env variable
- Check the database migration ran successfully

### "Could not reach the tutor service right now"
- Your API key might be invalid
- Gemini API might be temporarily down
- Check your internet connection

---

## 💰 Cost

- **Free tier**: 15 requests per minute, generous daily quota
- **Your cost**: $0 for up to ~500 active users with this 5-req/day limit
- **Paid tier**: If you exceed free quota, Gemini charges ~$0.0075 per 1K input tokens

For 5 requests/day × 500 users × 25 days/month ≈ 62,500 requests = ~$0.47/month at scale.

---

## 🔐 Security

- API key is only accessed on the server (never exposed to client)
- Student questions are sent to Google; review your privacy policy if needed
- Rate limiting prevents token depletion
- User context is optional and user-provided

---

## 📝 Customization

### Change the Tutor Prompt

Edit `src/server/actions/student/sat-tutor.ts` in the `callGeminiAPI` function:

```typescript
const prompt = `You are a friendly SAT tutor. A student is working on this question:
...
`;
```

### Change the Daily Limit

Edit the same file:
```typescript
const DAILY_LIMIT = 10; // e.g., 10 requests per day
```

### Change the Model

To use a different Gemini model (e.g., `gemini-pro`, `gemini-2-flash`):

```typescript
const GEMINI_MODEL = "gemini-2-flash"; // faster, cheaper
```

---

Need help? Check the component at `src/components/student/sat-tutor.tsx` or the action at `src/server/actions/student/sat-tutor.ts`.

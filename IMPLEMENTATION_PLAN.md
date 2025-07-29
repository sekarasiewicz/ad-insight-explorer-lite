# Ad Insights Explorer Lite - Implementation Plan

## Project Overview
This is a recruitment task for Mediaocean to create an ad insights dashboard that analyzes content from the JSONPlaceholder API to detect anomalies and provide insights for fraud detection and brand safety.

## Current Project Structure Analysis
The project already has a solid foundation with:
- **Backend**: Python Flask/FastAPI structure in `backend/`
- **Frontend**: React with Vite in `frontend/`
- **Docker**: Containerization setup for development and production
- **Testing**: Test infrastructure in place

## Implementation Plan

### Phase 1: Backend Development (1-1.5 hours)

#### 1.1 API Integration & Data Fetching
- [ ] Create service to fetch data from JSONPlaceholder API (`https://jsonplaceholder.typicode.com/posts`)
- [ ] Implement caching mechanism to avoid repeated API calls
- [ ] Add error handling for API failures

#### 1.2 Core Endpoints Implementation

**`/posts` Endpoint:**
- [ ] Fetch raw data from JSONPlaceholder API
- [ ] Return complete post data with proper error handling
- [ ] Add optional query parameters for pagination/filtering

**`/anomalies` Endpoint:**
- [ ] Implement anomaly detection logic:
  - Titles shorter than 15 characters
  - Duplicate titles by the same user
  - Users with more than 5 posts having similar titles (bot detection)
- [ ] Create data processing utilities for text analysis
- [ ] Return structured anomaly data with reasons for flagging

**`/summary` Endpoint:**
- [ ] Implement word frequency analysis across all post titles
- [ ] Calculate unique word count per user
- [ ] Return top 3 users with most unique words
- [ ] Return most frequently used words across all titles

#### 1.3 Data Models & Validation
- [ ] Define Pydantic models for request/response validation
- [ ] Create data transfer objects (DTOs) for API responses
- [ ] Add input validation and sanitization

### Phase 2: Frontend Development (1-1.5 hours)

#### 2.1 Dashboard Layout & Components
- [ ] Create main dashboard layout with responsive design
- [ ] Implement navigation and routing structure
- [ ] Design reusable UI components using existing shadcn/ui setup

#### 2.2 Anomalies Table Component
- [ ] Create data table component with:
  - User ID, Post ID, Title columns
  - Reason for flagging column
  - Filtering by userId
  - Sorting capabilities (by ID, title, user)
- [ ] Implement pagination for large datasets
- [ ] Add search/filter functionality

#### 2.3 Summary Panel Component
- [ ] Create summary dashboard showing:
  - Top 3 users with most unique words
  - Word frequency visualization (tag cloud or list)
  - Key metrics cards
- [ ] Implement data visualization components
- [ ] Add loading states and error handling

#### 2.4 API Integration & State Management
- [ ] Create API service layer using existing `services/api.ts`
- [ ] Implement React Query or SWR for data fetching
- [ ] Add proper error handling and loading states
- [ ] Implement data caching and refresh mechanisms

### Phase 3: Testing & Quality Assurance (30-45 minutes)

#### 3.1 Backend Testing
- [ ] Unit tests for anomaly detection algorithms
- [ ] API endpoint integration tests
- [ ] Data processing utility tests
- [ ] Error handling test cases

#### 3.2 Frontend Testing
- [ ] Component unit tests using existing test setup
- [ ] API integration tests
- [ ] User interaction tests
- [ ] Responsive design testing

#### 3.3 Performance Analysis
- [ ] Identify API bottlenecks and optimization opportunities
- [ ] Analyze UI performance issues
- [ ] Document areas for improvement
- [ ] Implement performance monitoring

### Phase 4: Polish & Documentation (15-30 minutes)

#### 4.1 UI/UX Enhancement
- [ ] Implement attractive styling using existing design system
- [ ] Add smooth animations and transitions
- [ ] Ensure responsive design across devices
- [ ] Implement dark/light mode support

#### 4.2 Documentation
- [ ] Update README with setup instructions
- [ ] Document API endpoints and usage
- [ ] Add code comments and documentation
- [ ] Create deployment guide

## Technical Implementation Details

### Backend Architecture
```
backend/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── posts.py
│   │   │   ├── anomalies.py
│   │   │   └── summary.py
│   │   └── models/
│   │       ├── post.py
│   │       ├── anomaly.py
│   │       └── summary.py
│   ├── services/
│   │   ├── jsonplaceholder_service.py
│   │   ├── anomaly_detector.py
│   │   └── text_analyzer.py
│   └── utils/
│       ├── cache.py
│       └── text_processing.py
```

### Frontend Architecture
```
frontend/src/
├── components/
│   ├── dashboard/
│   │   ├── Dashboard.tsx
│   │   ├── AnomaliesTable.tsx
│   │   └── SummaryPanel.tsx
│   ├── ui/
│   │   ├── data-table.tsx
│   │   ├── tag-cloud.tsx
│   │   └── metrics-card.tsx
│   └── common/
│       ├── LoadingSpinner.tsx
│       └── ErrorBoundary.tsx
├── services/
│   ├── api.ts (enhanced)
│   └── types.ts
└── hooks/
    ├── usePosts.ts
    ├── useAnomalies.ts
    └── useSummary.ts
```

## Key Features to Implement

### Anomaly Detection Logic
1. **Short Titles**: Filter posts with titles < 15 characters
2. **Duplicate Detection**: Find users with identical titles
3. **Bot Detection**: Identify users with >5 posts having similar titles (using text similarity algorithms)

### Text Analysis Features
1. **Word Frequency**: Count word occurrences across all titles
2. **Unique Word Analysis**: Calculate unique words per user
3. **Text Similarity**: Implement algorithms to detect similar titles

### UI/UX Features
1. **Responsive Design**: Mobile-first approach
2. **Interactive Tables**: Sortable, filterable data tables
3. **Visualizations**: Tag clouds, charts, and metrics cards
4. **Real-time Updates**: Auto-refresh capabilities

## Performance Considerations

### Backend Optimization
- Implement caching for API responses
- Use efficient text processing algorithms
- Add database indexing for large datasets
- Implement pagination for large result sets

### Frontend Optimization
- Use React.memo for expensive components
- Implement virtual scrolling for large tables
- Add debounced search functionality
- Optimize bundle size with code splitting

## Testing Strategy

### Backend Tests
- Unit tests for text processing algorithms
- Integration tests for API endpoints
- Performance tests for large datasets
- Error handling tests

### Frontend Tests
- Component unit tests
- Integration tests for API calls
- E2E tests for user workflows
- Performance tests for UI interactions

## Deployment Strategy

### Development Environment
- Use existing Docker setup
- Hot reload for both frontend and backend
- Environment-specific configurations

### Production Deployment
- Containerized deployment
- Environment variable management
- Health checks and monitoring
- CI/CD pipeline integration

## Success Criteria

### Functional Requirements
- [ ] All three API endpoints working correctly
- [ ] Anomaly detection accurately identifies flagged posts
- [ ] Summary data provides meaningful insights
- [ ] Frontend displays data correctly with filtering/sorting

### Non-Functional Requirements
- [ ] Response times under 2 seconds for all endpoints
- [ ] Responsive design works on all screen sizes
- [ ] Error handling provides meaningful feedback
- [ ] Code is well-documented and testable

### Extra Credit Features
- [ ] Performance analysis and optimization recommendations
- [ ] Comprehensive test coverage (>80%)
- [ ] Attractive and modern UI design
- [ ] Live demo deployment

## Timeline Breakdown

| Phase | Duration | Key Deliverables |
|-------|----------|------------------|
| Phase 1 | 1-1.5h | Working backend API with all endpoints |
| Phase 2 | 1-1.5h | Functional frontend dashboard |
| Phase 3 | 30-45m | Tests and performance analysis |
| Phase 4 | 15-30m | Polish and documentation |

**Total Estimated Time: 2-3 hours**

## Risk Mitigation

### Technical Risks
- **API Rate Limiting**: Implement caching and retry logic
- **Large Dataset Performance**: Use pagination and efficient algorithms
- **Text Processing Complexity**: Start with simple algorithms, optimize later

### Timeline Risks
- **Scope Creep**: Focus on core requirements first
- **Technical Debt**: Maintain clean code from the start
- **Testing Time**: Prioritize critical path testing

## Next Steps

1. **Immediate**: Set up development environment and review existing codebase
2. **Phase 1**: Start with backend API development
3. **Phase 2**: Build frontend components in parallel
4. **Phase 3**: Integrate and test end-to-end
5. **Phase 4**: Polish and prepare for submission

This plan provides a structured approach to implementing the Ad Insights Explorer Lite while leveraging the existing project infrastructure and following best practices for both backend and frontend development. 
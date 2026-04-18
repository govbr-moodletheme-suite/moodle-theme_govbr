(function () {
    const storageKey = 'dsgovbr-usability-lab-session';
    const textarea = document.getElementById('session-notes');
    const saveBtn = document.getElementById('save-notes');
    const downloadBtn = document.getElementById('download-notes');
    const downloadReportBtn = document.getElementById('download-report');
    const feedback = document.getElementById('notes-feedback');

    const participantId = document.getElementById('participant-id');
    const participantRole = document.getElementById('participant-role');
    const criticalErrors = document.getElementById('metric-critical-errors');
    const confidence = document.getElementById('metric-confidence');

    const scenarios = [
        { key: 'login', title: 'Login and First Impression' },
        { key: 'dashboard', title: 'Dashboard Orientation' },
        { key: 'course', title: 'Course Page Comprehension' },
        { key: 'settings', title: 'Theme Settings Discoverability' },
    ];

    if (!textarea || !saveBtn || !downloadBtn || !downloadReportBtn || !feedback) {
        return;
    }

    const readScenarioMetrics = function () {
        return scenarios.map(function (scenario) {
            const timeNode = document.getElementById('metric-time-' + scenario.key);
            const successNode = document.getElementById('metric-success-' + scenario.key);
            return {
                key: scenario.key,
                title: scenario.title,
                timeSeconds: Number(timeNode && timeNode.value ? timeNode.value : 0),
                success: Boolean(successNode && successNode.checked),
            };
        });
    };

    const collectState = function () {
        return {
            participant: {
                id: participantId ? participantId.value.trim() : '',
                role: participantRole ? participantRole.value : 'other',
            },
            metrics: {
                criticalErrors: Number(criticalErrors && criticalErrors.value ? criticalErrors.value : 0),
                confidence: Number(confidence && confidence.value ? confidence.value : 3),
                scenarios: readScenarioMetrics(),
            },
            notes: textarea.value,
        };
    };

    const persistState = function () {
        localStorage.setItem(storageKey, JSON.stringify(collectState()));
    };

    const previousRaw = localStorage.getItem(storageKey);
    if (previousRaw) {
        try {
            const previous = JSON.parse(previousRaw);
            if (previous.notes) {
                textarea.value = previous.notes;
            }
            if (participantId && previous.participant && previous.participant.id) {
                participantId.value = previous.participant.id;
            }
            if (participantRole && previous.participant && previous.participant.role) {
                participantRole.value = previous.participant.role;
            }
            if (criticalErrors && previous.metrics) {
                criticalErrors.value = previous.metrics.criticalErrors ?? 0;
            }
            if (confidence && previous.metrics) {
                confidence.value = previous.metrics.confidence ?? 3;
            }
            if (previous.metrics && Array.isArray(previous.metrics.scenarios)) {
                previous.metrics.scenarios.forEach(function (scenario) {
                    const timeNode = document.getElementById('metric-time-' + scenario.key);
                    const successNode = document.getElementById('metric-success-' + scenario.key);
                    if (timeNode) {
                        timeNode.value = scenario.timeSeconds ?? 0;
                    }
                    if (successNode) {
                        successNode.checked = Boolean(scenario.success);
                    }
                });
            }
        } catch (_error) {
            // Ignore invalid storage payload and start with empty form.
        }
    }

    saveBtn.addEventListener('click', function () {
        persistState();
        feedback.textContent = 'Notes saved locally.';
    });

    downloadBtn.addEventListener('click', function () {
        persistState();
        const payload = {
            exportedAt: new Date().toISOString(),
            path: window.location.pathname,
            notes: textarea.value,
        };
        const blob = new Blob([JSON.stringify(payload, null, 2)], {
            type: 'application/json',
        });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'usability-session-notes.json';
        link.click();
        URL.revokeObjectURL(url);
        feedback.textContent = 'JSON exported.';
    });

    downloadReportBtn.addEventListener('click', function () {
        persistState();

        const state = collectState();
        const scenarioCount = state.metrics.scenarios.length;
        const successCount = state.metrics.scenarios.filter(function (scenario) {
            return scenario.success;
        }).length;
        const totalTime = state.metrics.scenarios.reduce(function (sum, scenario) {
            return sum + scenario.timeSeconds;
        }, 0);

        const report = {
            exportedAt: new Date().toISOString(),
            participant: state.participant,
            summary: {
                successRate: scenarioCount > 0 ? successCount / scenarioCount : 0,
                totalTimeSeconds: totalTime,
                criticalErrors: state.metrics.criticalErrors,
                confidence: state.metrics.confidence,
            },
            scenarios: state.metrics.scenarios,
            notes: state.notes,
        };

        const idPart = state.participant.id || 'anonymous';
        const blob = new Blob([JSON.stringify(report, null, 2)], {
            type: 'application/json',
        });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'participant-report-' + idPart + '.json';
        link.click();
        URL.revokeObjectURL(url);
        feedback.textContent = 'Participant report exported.';
    });
})();

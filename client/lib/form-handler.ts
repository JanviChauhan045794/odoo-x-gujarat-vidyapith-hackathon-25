import { toast } from 'sonner';

interface FormResponse {
    status: string;
    message: string;
}

export class UtilityHandler {

    static async onSubmitPost<T>(url: string, data: T): Promise<void> {
        toast.info('Submitting form with data: ' + JSON.stringify(data));
        const toastId = toast.loading('Submitting Form');
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
            const result: FormResponse = await response.json();
            if (!response.ok) {
                toast.error(`Server response with status ${response.status}`);
            }
            if (result.status === 'error') {
                toast.error(result.message);
            } else {
                toast.success('Form submitted successfully');
            }
        } catch (error) {
            toast.error('An error occurred: ' + (error instanceof Error ? error.message : error));
        } finally {
            toast.dismiss(toastId); // Dismiss toast after the request is completed
        }
    }
}
